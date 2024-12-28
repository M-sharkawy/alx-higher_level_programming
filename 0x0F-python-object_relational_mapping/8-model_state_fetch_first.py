#!/usr/bin/python3
"""module to prints the first State
object from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
import MySQLdb

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).first()

    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")

    session.close()
