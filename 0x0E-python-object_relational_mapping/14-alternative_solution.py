#!/usr/bin/python3
"""
find all states with 'a' in it
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city_name, state_name, city_id in session.query(
            City.name, State.name, City.id).join(State):
        print("{}: ({}) {}".format(state_name, city_id, city_name))
