import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_directory = os.path.join(os.path.dirname(__file__), 'db')
os.makedirs(db_directory, exist_ok=True)

DATABASE_URL = os.path.join(db_directory, "clients.db")

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String,  nullable=False)
    password = Column(String, nullable=False)
    code = Column(String(6), nullable=False)


engine = create_engine(f"sqlite:///{DATABASE_URL}")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


DATABASE_URL = os.path.join(db_directory, "workers.db")

Base = declarative_base()

class Worker(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

engine = create_engine(f"sqlite:///{DATABASE_URL}")
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)



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