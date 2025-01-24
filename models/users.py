from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base



class Users(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_name_surname = Column(String, nullable=True)
    pc_id = Column(Integer, ForeignKey('Pcs.pc_id'), nullable=False)
    user_time = Column(String)

    pcs = relationship('Pcs', back_populates='us')