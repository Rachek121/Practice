import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QScrollArea, QGridLayout, QMessageBox)
from PyQt6.QtGui import QPixmap
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


db_directory = os.path.join(os.path.dirname(__file__), '..', 'db')
DATABASE_URL = os.path.join(db_directory, "rental_cars.db")

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    client_id = Column(String, nullable=False)
    rental_duration = Column(Integer, nullable=False)

engine = create_engine(f"sqlite:///{DATABASE_URL}")
SessionLocal = sessionmaker(bind=engine)

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
        self.cars = [
            {"image": "car1.png", "info": "Информация о машине 1", "status": "Свободен", "name": "A80"},
            {"image": "car2.png", "info": "Информация о машине 2", "status": "Свободен", "name": "Машина 2"},
            {"image": "car3.png", "info": "Информация о машине 3", "status": "Свободен", "name": "Машина 3"},
        ]

        for idx, car in enumerate(self.cars):
            image_label = QLabel()
            pixmap = QPixmap(car["image"])
            image_label.setPixmap(pixmap.scaled(150, 100))

            check_button = QPushButton("Проверить")
            info_button = QPushButton("Информация об автомобиле")

            check_button.setProperty("car_name", car["name"])
            info_button.setProperty("car_info", car["info"])

            check_button.clicked.connect(self.check_car_status)
            info_button.clicked.connect(self.show_info)

            self.car_layout.addWidget(image_label, idx, 0)
            self.car_layout.addWidget(check_button, idx, 1)
            self.car_layout.addWidget(info_button, idx, 2)

    def check_car_status(self):
        button = self.sender()
        car_name = button.property("car_name")

        session = SessionLocal()
        cars_in_db = session.query(Car).filter(Car.name == car_name).first()
        session.close()

        if cars_in_db:
            QMessageBox.information(self, "Статус автомобиля", f"Автомобиль '{car_name}': Занят")
        else:
            QMessageBox.information(self, "Статус автомобиля", f"Автомобиль '{car_name}': Свободен")

    def show_info(self):
        button = self.sender()
        info = button.property("car_info")
        QMessageBox.information(self, "Информация об автомобиле", info)
