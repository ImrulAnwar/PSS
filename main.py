import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QGuiApplication

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    # Calculate the size and position of the window
    screen = QGuiApplication.primaryScreen()
    screen_rect = screen.geometry()
    width = int(screen_rect.width() * 0.6)
    height = int(width / 16 * 9)
    x = int((screen_rect.width() - width) / 2)
    y = int((screen_rect.height() - height) / 2)

    # Set the size and position of the window
    win.setGeometry(x, y, width, height)
    win.setWindowTitle("Database")
    win.show()
    sys.exit(app.exec_())



window()