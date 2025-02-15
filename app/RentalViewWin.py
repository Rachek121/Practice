import os
from PyQt6 import QtWidgets, QtCore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Установка директории для базы данных
db_directory = os.path.join(os.path.dirname(__file__), 'db')
os.makedirs(db_directory, exist_ok=True)
DATABASE_URL = os.path.join(db_directory, "rental_cars.db")

# Определяем базу данных
Base = declarative_base()


# Определяем модель для таблицы 'cars'
class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    client_id = Column(String, nullable=False)
    rental_duration = Column(Integer, nullable=False)


# Создаем движок и сессию
engine = create_engine(f"sqlite:///{DATABASE_URL}")
SessionLocal = sessionmaker(bind=engine)


class RentalViewApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rental Cars Information")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QtWidgets.QVBoxLayout()

        self.table = QtWidgets.QTableWidget()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

        self.load_data()

    def load_data(self):
        session = SessionLocal()
        cars = session.query(Car).all()
        self.table.setRowCount(len(cars))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Client ID", "Rental Duration (days)"])

        for row_idx, car in enumerate(cars):
            self.table.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(str(car.id)))
            self.table.setItem(row_idx, 1, QtWidgets.QTableWidgetItem(car.name))
            self.table.setItem(row_idx, 2, QtWidgets.QTableWidgetItem(car.client_id))
            self.table.setItem(row_idx, 3, QtWidgets.QTableWidgetItem(str(car.rental_duration)))

        session.close()