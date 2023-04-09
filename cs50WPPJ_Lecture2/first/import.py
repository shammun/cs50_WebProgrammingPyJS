import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:ShPyR13_@localhost:5432/my_database")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for ori, des, dur in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin": ori, "destination": des, "duration": dur})
        print(f"Added flight from {ori} to {des} lasting {dur} minutes.")
    db.commit() # If I am reading data, this is not needed

if __name__ == "__main__":
    main()
