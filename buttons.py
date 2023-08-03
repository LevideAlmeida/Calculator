from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import SMALL_FONT_SIZE
from utils import isNumOrDot, isValidNumber
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from info import Info
    from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(SMALL_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(70, 70)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', 'expand', '.', '='],
        ]

        self.display = display
        self.info = info
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, button_name in enumerate(row):
                button = Button(button_name)

                if button_name == '0':
                    self.addWidget(button, i, j, 1, 2)
                if button_name == 'expand':
                    continue

                if not isNumOrDot(button_name):
                    button.setProperty(
                        'cssClass', 'specialButton')  # type: ignore

                self.addWidget(button, i, j)

                slot = self._makeSlot(self._insertTextInDisplay, button)
                self._connectButtonClicked(button, slot)

                self._configSpecialButton(button)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self, button: Button):
        buttonText = button.text()

        if buttonText == 'C':
            self._connectButtonClicked(button, self._clear)

        if buttonText in '+-*/':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._operatorClicked, button))

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertTextInDisplay(self, button: Button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.display.clear()

    def _operatorClicked(self, button: Button):
        displayText = self.display.text()
        print(displayText, type(displayText))

        # if user used operator without insert a number
        if displayText != '' and self._left is None:
            self._left = self.display.text()

            self._left = float(
                self._left) if '.' in self._left else int(self._left)

            print(f'{self._left}', type(self._left))

        self._op = button.text()
        self.equation = f'{self._left} {self._op} '

        if self._left is None and displayText == '':
            self.equation = 'Expressão mal formada'

        self.display.clear()
