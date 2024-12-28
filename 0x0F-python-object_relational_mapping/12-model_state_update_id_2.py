#!/usr/bin/python3
"""module that changes the name of a State object from the database"""

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

    new_entery = session.query(State).filter(State.id == 2).first()

    new_entery.name = "New Mexico"

    session.commit()

    session.close()
