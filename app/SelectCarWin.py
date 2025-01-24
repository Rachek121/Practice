from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QScrollArea, QGridLayout, QMessageBox)
from PyQt6.QtGui import QPixmap

class CarWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Автомобили")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.car_container = QWidget()
        self.car_layout = QGridLayout()

        self.setup_cars()

        self.car_container.setLayout(self.car_layout)
        self.scroll_area.setWidget(self.car_container)
        self.layout.addWidget(self.scroll_area)
        self.setLayout(self.layout)

    def setup_cars(self):
        cars = [
            {"image": "car1.png", "info": "Информация о машине 1"},
            {"image": "car2.png", "info": "Информация о машине 2"},
            {"image": "car3.png", "info": "Информация о машине 3"},
        ]

        for idx, car in enumerate(cars):
            image_label = QLabel()
            pixmap = QPixmap(car["image"])
            image_label.setPixmap(pixmap.scaled(150, 100))

            order_button = QPushButton("Заказать")
            info_button = QPushButton("Информация об автомобиле")


            order_button.setProperty("car_info", car["info"])
            info_button.setProperty("car_info", car["info"])
            order_button.clicked.connect(self.order_car)
            info_button.clicked.connect(self.show_info)

            self.car_layout.addWidget(image_label, idx, 0)
            self.car_layout.addWidget(order_button, idx, 1)
            self.car_layout.addWidget(info_button, idx, 2)

    def order_car(self):
        QMessageBox.information(self, "Заказ автомобиля", "Выделите автомобиль для заказа!")

    def show_info(self):

        button = self.sender()
        info = button.property("car_info")
        QMessageBox.information(self, "Информация об автомобиле", info)
