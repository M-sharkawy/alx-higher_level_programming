#!/usr/bin/python3
"""module to  lists all State objects from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = session()

    states = session.query(State, City) \
        .filter(State.id == City.state_id).order_by(City.id).all()

    for state, city in states:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
