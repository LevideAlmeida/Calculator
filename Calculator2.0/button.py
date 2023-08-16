from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING
from values import SMALL_TEXT_SIZE
from tools import isNumOrDot, isValidCaracter

if TYPE_CHECKING:
    from lineEdit import Display
    from msgData import Historic, Status


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(SMALL_TEXT_SIZE)
        self.setFont(font)
        self.setMinimumSize(70, 70)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', historic: 'Historic',
                 status: 'Status', parent=None):
        super().__init__(parent)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', 'expand', '.', '=']
        ]
        self.display = display
        self.historic = historic
        self.status = status
        self._makeGrid()

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.backspacePressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertValueInDisplay)

        for i, row in enumerate(self._gridMask):
            for j, column in enumerate(row):
                button = Button(column)
                buttonText = button.text()

                if column == '0':
                    self.addWidget(button, i, j, 1, 2)
                if column == 'expand':
                    continue

                if not isNumOrDot(buttonText):
                    button.setProperty(
                        'cssClass', 'specialButton')  # type: ignore

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertValueInDisplay, buttonText)
                self._connectButtonClicked(button, slot)

                self._configSpecialButton(button)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        buttonName = button.text()

        if buttonName == 'C':
            self._connectButtonClicked(button, self._clear)

        if buttonName == '◀':
            self._connectButtonClicked(button, self._backspace)

        if buttonName == '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def _realSlot(_):
            func(*args, **kwargs)
        return _realSlot

    @Slot()
    def _insertValueInDisplay(self, text: str):

        if not isValidCaracter(text):
            return

        newDisplayValue = self.display.text() + text

        if '**' in newDisplayValue:
            newDisplayValue = newDisplayValue.replace('**', '^')

        self.display.setText(newDisplayValue)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    @Slot()
    def _eq(self):
        equation = self.display.text()
        self.status.setText('')

        if len(equation) == 0:
            return

        result = ''

        try:
            if '^' in equation:
                result = eval(equation.replace('^', '**'))
            else:
                result = eval(equation)

            self.historic.insertEquation(f'{equation} = {result}')
            self.display.setText(f'{result}')
            self.equationValues = []

        except SyntaxError:
            self.status.setText('Expressão mal formada')

        self.display.setFocus()
