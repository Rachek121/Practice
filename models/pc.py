from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Pcs(Base):
    __tablename__ = 'Pcs'

    pc_id = Column(Integer, primary_key=True, index=True)
    pc_name = Column(String, nullable=True)

    us = relationship('Users', back_populates='pcs')


