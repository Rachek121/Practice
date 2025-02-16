import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
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

class RentalViewWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Просмотр прокатов")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Название машины", "ID Клиента", "Срок аренды (дни)"])

        self.btn_refresh = QPushButton("Обновить")
        self.btn_refresh.clicked.connect(self.load_cars)

        self.layout.addWidget(self.table)
        self.layout.addWidget(self.btn_refresh)

        self.setLayout(self.layout)

        self.load_cars()

    def load_cars(self):
        session = SessionLocal()
        cars = session.query(Car).all()

        self.table.setRowCount(len(cars))
        row_index = 0
        for car in cars:
            self.table.setItem(row_index, 0, QTableWidgetItem(str(car.id)))
            self.table.setItem(row_index, 1, QTableWidgetItem(car.name))
            self.table.setItem(row_index, 2, QTableWidgetItem(car.client_id))
            self.table.setItem(row_index, 3, QTableWidgetItem(str(car.rental_duration)))
            row_index += 1

        session.close()

        if len(cars) == 0:
            QMessageBox.information(self, "GAIJIN", "Нет доступных прокатов!")
