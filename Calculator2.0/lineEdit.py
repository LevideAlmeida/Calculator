from PySide6.QtWidgets import QLineEdit
from values import TEXT_MARGIN, MINIMUN_WIDTH, BIG_TEXT_SIZE
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._configStyle()

    def _configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_TEXT_SIZE}px')
        self.setMinimumSize(MINIMUN_WIDTH, BIG_TEXT_SIZE + TEXT_MARGIN*2)
        self.setTextMargins(*margins)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # type: ignore
