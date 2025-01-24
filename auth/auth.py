from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWindow
import sys

true_username = "1"
true_password = "1"

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.resize(270, 100)
        self.setWindowIcon(QIcon(''))

        layout = QVBoxLayout()

        self.label_username = QLabel("Логин:")
        self.entry_username = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.entry_username)

        self.label_password = QLabel("Пароль:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.entry_password)

        self.button_login = QPushButton("Войти")
        self.button_login.clicked.connect(self.login)
        self.button_quit = QPushButton("Выйти из приложения")
        self.button_quit.clicked.connect(self.close)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_quit)

        self.setLayout(layout)


    def login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if username == true_username and password == true_password:
            QMessageBox.information(self, "Все верно", "Вход выполнен")
            self.open_main_window()
        else:
            QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль.")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
