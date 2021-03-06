#!/usr/bin/python3
"""
find all states with 'a' in it
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    louisiana_state = State(name="Louisiana")
    session.add(louisiana_state)
    session.commit()
    for row in session.query(State).filter_by(name="Louisiana"):
        print("{:d}".format(row.id))
