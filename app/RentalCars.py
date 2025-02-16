import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QSpinBox


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
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


class AddCarWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Добавить машину")
        self.setGeometry(100, 100, 300, 250)

        self.layout = QVBoxLayout()

        self.label_name = QLabel("Название машины:")
        self.input_name = QLineEdit()

        self.label_client = QLabel("ID Клиента:")
        self.input_client = QLineEdit()

        self.label_rental_duration = QLabel("Срок аренды (дни):")
        self.input_rental_duration = QSpinBox()
        self.input_rental_duration.setMinimum(1)  # Минимум 1 день
        self.input_rental_duration.setMaximum(365)

        self.btn_add = QPushButton("Добавить")
        self.btn_add.clicked.connect(self.add_car)

        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.label_client)
        self.layout.addWidget(self.input_client)
        self.layout.addWidget(self.label_rental_duration)
        self.layout.addWidget(self.input_rental_duration)
        self.layout.addWidget(self.btn_add)

        self.setLayout(self.layout)

    def add_car(self):
        name = self.input_name.text()
        client = self.input_client.text()
        rental_duration = self.input_rental_duration.value()

        if not name or not client:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля!")
            return

        session = SessionLocal()
        new_car = Car(name=name, client_id=client, rental_duration=rental_duration)
        session.add(new_car)
        session.commit()
        session.close()

        QMessageBox.information(self, "Успешно", f"Машина '{name}' добавлена для клиента '{client}' на {rental_duration} дней!")
        self.close()
