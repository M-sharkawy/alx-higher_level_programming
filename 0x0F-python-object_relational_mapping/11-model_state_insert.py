#!/usr/bin/python3
"""module that adds the State object “Louisiana” to the database"""

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

    new_insert = State(name="Louisiana")

    session.add(new_insert)

    session.commit()

    print(f"{new_insert.id}")

    session.close()
