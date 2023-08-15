from PySide6.QtWidgets import QLabel, QWidget
from typing import Optional
from values import NORMAL_TEXT_SIZE, MINIMUN_WIDTH
from PySide6.QtCore import Qt


class Historic(QLabel):
    def __init__(self, text: str, widget: Optional[QWidget] = None) -> None:
        super().__init__(text, widget)
        self.configStyle()
        self.historic = []

    def configStyle(self):
        self.setStyleSheet(f'font-size: {NORMAL_TEXT_SIZE}px')
        self.setMinimumSize(MINIMUN_WIDTH, 200)
        self.setAlignment(Qt.AlignmentFlag.AlignTrailing)  # type: ignore

    def insertEquation(self, equation: str):
        self.historic.append(equation)
        if len(self.historic) > 7:
            self.historic.pop(0)

        text = '\n'.join(self.historic)
        self.setText(text)


class Status(QLabel):
    def __init__(self, text: str, widget: Optional[QWidget] = None) -> None:
        super().__init__(text, widget)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {NORMAL_TEXT_SIZE}; color: red;')
        self.setMinimumSize(MINIMUN_WIDTH, NORMAL_TEXT_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # type: ignore
