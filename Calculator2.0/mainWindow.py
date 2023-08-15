from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.cw = QWidget()
        self.setCentralWidget(self.cw)

        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)

        self.setWindowTitle('Calculator')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
