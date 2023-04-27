from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from datetime import date
from plusbus_data import Customers, Journeys, Bookings, Base

from sqlalchemy.engine import Engine
from sqlalchemy import event


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Database = 'sqlite:///plusbus.db'


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Customers(email="klement@gmail.com", phone=20201030))
        new_items.append(Customers(email="fortniteKlement@gmail.com", phone=20105020))
        new_items.append(Customers(email="torben@gmail.com", phone=45102014))
        a_date = date(day=23, month=12, year=2023)
        new_items.append(Journeys(route="Høje Taastrup, København", date=a_date, max_capacity=12))
        a_date = date(day=10, month=1, year=2024)
        new_items.append(Journeys(route="København, Roskilde", date=a_date, max_capacity=6))
        new_items.append(Bookings(customer_id=2, journey_id=1, capacity=2))
        new_items.append(Bookings(customer_id=1, journey_id=1, capacity=3))
        session.add_all(new_items)
        session.commit()


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)

        return result


def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


def create_record_customer(record):
    with Session(engine) as session:
        print(record)
        record.entry_customer_id = None
        session.add(record)
        try:
            session.commit()
        except:
            print("There was an error while creating a record")


def update_customer(customer):
    with Session(engine) as session:
        session.execute(update(Customers).where(Customers.id == customer.id).values(email=customer.email, phone=customer.phone))
        session.commit()


def soft_delete_customer(customer):
    with Session(engine) as session:
        session.execute(update(Customers).where(Customers.id == customer.id).values(email="deleted", phone=customer.phone))
        session.commit()


def create_record_journey(record):
    with Session(engine) as session:
        print(record)
        record.entry_journey_id = None
        print(record)
        session.add(record)
        try:
            session.commit()
        except:
            print("There was an error while creating a record")
def update_journey(journey):
    with Session(engine) as session:
        session.execute(update(Journeys).where(Journeys.id == journey.id).values(route=journey.route, date=journey.date, max_capacity=journey.max_capacity))
        session.commit()


def soft_delete_journey(journey):
    with Session(engine) as session:
        session.execute(update(Journeys).where(Journeys.id == journey.id).values(route=journey.route, date=journey.date, max_capacity=-1))
        session.commit()


if __name__ == "__main__":  # Executed when invoked directly
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)
    print(get_record(Customers, 1))
    print(get_record(Journeys, 2))
    print(get_record(Bookings, 2))
    print(select_all(Customers))

else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)
