import traceback
from PyQt6.QtWidgets import QApplication
from auth.auth import LoginWindow
import sys

def main():
    app = QApplication([])
    win = LoginWindow()
    win.show()
    sys.exit(app.exec())


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))


sys.excepthook = excepthook

if __name__ == '__main__':
    main()
