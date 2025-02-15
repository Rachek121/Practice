from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database import SessionLocal, Worker

class AddWorkerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавить работника")
        self.setGeometry(100, 100, 300, 300)

        self.layout = QVBoxLayout()

        self.label_name = QLabel("Имя:")
        self.input_name = QLineEdit()

        self.label_position = QLabel("Должность:")
        self.input_position = QLineEdit()

        self.label_login = QLabel("Логин:")
        self.input_login = QLineEdit()

        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)  # Скрываем ввод пароля

        self.btn_add = QPushButton("Добавить")
        self.btn_add.clicked.connect(self.add_worker)

        # Добавляем все элементы в layout
        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.label_position)
        self.layout.addWidget(self.input_position)
        self.layout.addWidget(self.label_login)
        self.layout.addWidget(self.input_login)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.btn_add)

        self.setLayout(self.layout)

    def add_worker(self):
        name = self.input_name.text()
        position = self.input_position.text()
        login = self.input_login.text()
        password = self.input_password.text()

        if not (name and position and login and password):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        db = SessionLocal()
        new_worker = Worker(name=name, position=position, login=login, password=password)

        try:
            db.add(new_worker)
            db.commit()
            QMessageBox.information(self, "Успех", f"Работник '{name}' добавлен!")
            self.close()
        except Exception as e:
            db.rollback()
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить работника: {e}")
        finally:
            db.close()
