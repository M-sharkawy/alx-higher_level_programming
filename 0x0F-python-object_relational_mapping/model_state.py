#!/usr/bin/python3
"""Module use sqlalchemy to create state table in the database"""

from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class states"""
    __tablename__ = "states"
    id = column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = column(String(128), nullable=False)
