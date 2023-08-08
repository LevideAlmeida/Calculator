from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import SMALL_FONT_SIZE
from utils import isNumOrDot, isValidNumber, convertToNumber
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING
import math

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
        self.display.eqPressed.connect(self._eq)
        self.display.backspacePressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertTextInDisplay)
        self.display.operatorPressed.connect(self._configOperator)

        for i, row in enumerate(self._gridMask):
            for j, buttonName in enumerate(row):
                button = Button(buttonName)

                if buttonName == '0':
                    self.addWidget(button, i, j, 1, 2)
                if buttonName == 'expand':
                    continue

                if not isNumOrDot(buttonName):
                    button.setProperty(
                        'cssClass', 'specialButton')  # type: ignore

                self.addWidget(button, i, j)

                slot = self._makeSlot(self._insertTextInDisplay, buttonName)
                self._connectButtonClicked(button, slot)

                self._configSpecialButton(button)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)  # type: ignore

    def _configSpecialButton(self, button: Button):
        buttonText = button.text()

        if buttonText == 'C':
            self._connectButtonClicked(button, self._clear)

        if buttonText in '+-*/^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configOperator, buttonText))

        if buttonText == '=':
            self._connectButtonClicked(button, self._eq)

        if buttonText == '◀':
            self._connectButtonClicked(button, self._backspace)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _insertTextInDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.display.clear()
        self.equation = ''
        self.display.setFocus()

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    @Slot()
    def _configOperator(self, operator):
        displayText = self.display.text()

        # clear the display if there is a '-' in the display
        if displayText == '-' and operator != '-':
            self.display.clear()
            displayText = self.display.text()

        # change operator if there is a '-' in the display
        if displayText == '-' and operator == '-':
            if self._op != '-' and self._op is not None:
                self._op = operator
                self.equation = f'{self._left} {self._op} '
                self.display.clear()
            else:
                return

        # if have a _left but not have a _op, self._left receive displayText
        if self._left is not None and self._op is None:
            self._left = convertToNumber(displayText)

        # if user used operator without insert a number
        if displayText != '' and self._left is None:
            self._left = convertToNumber(displayText)

        # return if doesn't have a value to self._left
        if displayText == '' and self._left is None:
            if operator == '-':
                self.display.insert(operator)
                displayText = self.display.text()

            return

        # insert '-' in display if display is empty
        if displayText == '' and self._left is not None:
            if operator == '-':
                self.display.insert(operator)
                displayText = self.display.text()

        if displayText != '-':
            self._op = operator
            self.equation = f'{self._left} {self._op} '
            self.display.clear()

        self.display.setFocus()

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        if self._op is None:
            self._left = convertToNumber(displayText)
            self.equation = f'{self._left} = {self._left}'
            self.display.clear()
            return

        if self._right is None:
            self._right = convertToNumber(displayText)

        self.equation = f'{self._left} {self._op} {self._right}'
        result = ''

        try:

            if '^' in self.equation and self._left is not None:
                result = str(math.pow(self._left, self._right)) + ' '
            else:
                result = str(eval(self.equation)) + ' '

            if '.0 ' in result:
                result = result.replace('.0 ', '')
            else:
                result = result.replace(' ', '')

            self.display.setText(f'{result}')
            self._left = convertToNumber(result)
            self.equation = f'{self._left}'
            self._op = None
            self._right = None

        except ZeroDivisionError:
            self._clear()
            self.equation = 'Impossivel dividir por zero'
        except OverflowError:
            self._clear()
            self.equation = 'Incalculavel'
        except ValueError:
            self._left = float(result)
            self.equation = f'{self._left}'

        self.display.setFocus()
