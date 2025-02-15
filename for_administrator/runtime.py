import sys
from PyQt6.QtWidgets import QApplication
from AddWorkerWindow import AddWorkerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    add_worker_window = AddWorkerWindow()
    add_worker_window.show()

    sys.exit(app.exec())
