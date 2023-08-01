from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget
from typing import Optional
from variables import SMALL_FONT_SIZE


class Info(QLabel):
    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        super().__init__(text, parent)
        self.configStyle()
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # type: ignore

    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
