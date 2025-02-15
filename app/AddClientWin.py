from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class AddClientWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавить клиента")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label_login = QLabel("Логин:")
        self.input_login = QLineEdit()

        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)  # Скрытие пароля

        self.btn_add = QPushButton("Добавить")
        self.btn_add.clicked.connect(self.add_client)

        self.layout.addWidget(self.label_login)
        self.layout.addWidget(self.input_login)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.btn_add)

        self.setLayout(self.layout)

    def add_client(self):
        login = self.input_login.text()
        password = self.input_password.text()


        QMessageBox.information(self, "GAIJIN", f"Клиент с логином {login} добавлен!")
        self.close()
