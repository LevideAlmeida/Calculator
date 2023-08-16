from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from values import TEXT_MARGIN, MINIMUN_WIDTH, BIG_TEXT_SIZE
from tools import isNumOrDot


class Display(QLineEdit):
    eqPressed = Signal()
    backspacePressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._configStyle()

    def _configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_TEXT_SIZE}px')
        self.setMinimumSize(MINIMUN_WIDTH, BIG_TEXT_SIZE + TEXT_MARGIN*2)
        self.setTextMargins(*margins)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # type: ignore

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text()
        key = event.key()
        KEYS = Qt.Key
        arrows = [KEYS.Key_Up, KEYS.Key_Down, KEYS.Key_Right, KEYS.Key_Left]

        if key == KEYS.Key_Backspace:
            self.backspacePressed.emit()
            return event.ignore()

        elif key in [KEYS.Key_Return, KEYS.Key_Enter, KEYS.Key_Equal]:
            self.eqPressed.emit()
            return event.ignore()

        elif key == KEYS.Key_Escape:
            self.clearPressed.emit()
            return event.ignore()

        elif isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()

        elif len(text) == 0:
            self.setFocus()
            return event.ignore()

        elif key == KEYS.Key_Delete:
            return super().keyPressEvent(event)

        elif key in arrows:
            return super().keyPressEvent(event)

        elif text in '+-/*^':
            self.inputPressed.emit(text)
            return event.ignore()
