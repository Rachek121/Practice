import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
from app.MainWin import MainWindow
from database import Worker
import sys


db_directory = os.path.join(os.path.dirname(__file__), '..', 'db')
DATABASE_URL = os.path.join(db_directory, "workers.db")


engine = create_engine(f"sqlite:///{DATABASE_URL}")
SessionLocal = sessionmaker(bind=engine)

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


        session = SessionLocal()
        try:
            worker = session.query(Worker).filter_by(login=username, password=password).first()
            if worker:
                QMessageBox.information(self, "Все верно", f"Вход выполнен")
                self.open_main_window()
            else:
                QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка доступа к базе данных: {e}")
        finally:
            session.close()

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()