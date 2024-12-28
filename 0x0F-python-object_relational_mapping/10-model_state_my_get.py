#!/usr/bin/python3
"""module prints the State object
with the name passed as argument from the database"""

import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = session()

    states = session.query(State) \
        .filter(State.name == {sys.argv[4]}).one_or_none()

    if states is None:
        print("Not found")
    else:
        print(states.id)

    session.close()
