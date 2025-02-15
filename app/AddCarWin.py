from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QSpinBox

class AddCarWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавить машину")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        self.label_name = QLabel("Название машины:")
        self.input_name = QLineEdit()

        self.label_price = QLabel("Стоимость:")
        self.input_price = QLineEdit()

        self.label_rental_duration = QLabel("Срок аренды (дни):")
        self.input_rental_duration = QSpinBox()
        self.input_rental_duration.setMinimum(1)  # Минимум 1 день

        self.btn_add = QPushButton("Добавить")
        self.btn_add.clicked.connect(self.add_car)

        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.label_price)
        self.layout.addWidget(self.input_price)
        self.layout.addWidget(self.label_rental_duration)
        self.layout.addWidget(self.input_rental_duration)
        self.layout.addWidget(self.btn_add)

        self.setLayout(self.layout)

    def add_car(self):
        name = self.input_name.text()
        price = self.input_price.text()
        rental_duration = self.input_rental_duration.value()


        QMessageBox.information(self, "GAIJIN", f"Машина '{name}' добавлена на {rental_duration} дней!")
        self.close()
