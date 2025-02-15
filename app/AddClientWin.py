from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database import SessionLocal, Client

class AddClientWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавить клиента")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        self.label_login = QLabel("Логин:")
        self.input_login = QLineEdit()

        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_code = QLabel("Шестизначный код:")
        self.input_code = QLineEdit()
        self.input_code.setMaxLength(6)

        self.btn_add = QPushButton("Добавить")
        self.btn_add.clicked.connect(self.add_client)

        self.layout.addWidget(self.label_login)
        self.layout.addWidget(self.input_login)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.label_code)
        self.layout.addWidget(self.input_code)
        self.layout.addWidget(self.btn_add)

        self.setLayout(self.layout)

    def add_client(self):
        login = self.input_login.text()
        password = self.input_password.text()
        code = self.input_code.text()

        if not login or not password or not code:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        if len(code) != 6:
            QMessageBox.warning(self, "Ошибка", "Код должен состоять из 6 символов.")
            return

        db = SessionLocal()
        new_client = Client(login=login, password=password, code=code)

        try:
            db.add(new_client)
            db.commit()
            QMessageBox.information(self, "Успех", f"Клиент '{login}' добавлен с кодом '{code}'!")
            self.close()
        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить клиента: {e}")
        finally:
            db.close()
