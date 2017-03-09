#!/usr/bin/python3
"""
displays all state objects from a given database
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    if instance = session.query(State).first():
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
