from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import SMALL_FONT_SIZE
from utils import isNumOrDot
from display import Display
from PySide6.QtCore import Slot


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
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', 'expand', '.', '='],
        ]

        self.display = display
        self._makeGrid()

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

                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertTextInDisplay,
                    button,
                )

                button.clicked.connect(buttonSlot)  # type: ignore

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertTextInDisplay(self, button: Button):
        buttonText = button.text()
        self.display.insert(buttonText)
