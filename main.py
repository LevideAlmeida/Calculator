import sys
from PySide6.QtWidgets import QApplication, QLabel
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    text = QLabel('TEXTO')
    text.setStyleSheet('font-size: 150px; color: red;')

    window.grid_layout.addWidget(text)

    window.adjustFixedSize()

    window.show()

    app.exec()
