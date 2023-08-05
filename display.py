from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit
from variables import MEDIUM_FONT_SIZE, TEXT_MARGIN, MINIMUN_WIDTH
from PySide6.QtCore import Qt, Signal


class Display(QLineEdit):
    eqPressed = Signal()
    backspacePressed = Signal()
    clearPressed = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        self.setMinimumHeight(MEDIUM_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # type: ignore
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent):
        text = event.text()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isBackspace = key == KEYS.Key_Backspace
        isESC = key == KEYS.Key_Escape

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        elif isBackspace:
            self.backspacePressed.emit()
            return event.ignore()

        elif isESC:
            self.clearPressed.emit()
            return event.ignore()

        if len(text) == 0:
            return event.ignore()

        print('texto', text)
