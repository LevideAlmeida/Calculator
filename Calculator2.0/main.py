from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from mainWindow import MainWindow
from msgData import Historic, Status
from lineEdit import Display
from button import ButtonsGrid
from values import ICON_FILE
from theme import setup_theme
import sys

if __name__ == '__main__':
    # Create application
    app = QApplication(sys.argv)

    # Apply theme
    setup_theme()

    # Main Window
    window = MainWindow()

    # Icon
    icon = QIcon(str(ICON_FILE))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    # Historic
    historic = Historic('')
    window.vLayout.addWidget(historic)

    # Display
    display = Display()
    window.vLayout.addWidget(display)

    # Status
    status = Status('')
    window.vLayout.addWidget(status)

    # Add buttons grid
    buttonsGrid = ButtonsGrid(display, historic, status)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
