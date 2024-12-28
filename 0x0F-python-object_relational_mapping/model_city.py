#!/usr/bin/python3
"""module construct class city"""

from model_state import Base, State
from sqlalchemy import ForeignKey, Column, String, Integer


class City(Base):
    """Class City"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
