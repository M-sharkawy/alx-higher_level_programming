#!/usr/bin/python3
"""module to  lists all State objects from the database hbtn_0e_6_usa"""

import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = session()

    states = session.query(State).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
