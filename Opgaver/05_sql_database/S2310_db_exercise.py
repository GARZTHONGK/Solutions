"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny database "my_second_sql_database.db" i din eksisterende mappe “data”.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() til begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Der skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""
from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select
from sqlalchemy import Float

Database = 'sqlite:///../data/my_second_sql_database.db'
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"  # gives table a name
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Customer({self.id=}    {self.name=}    {self.age=})"

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Float)
    brand = Column(String)
    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Product({self.id=}    {self.product_number=}    {self.price=}    {self.brand=})"


def create_test_data():
    with Session(engine) as session:
        data = []

        # Customer data
        data.append(Customer(name='Torben', address='Villa vej 23', age=23))
        data.append(Customer(name='Frederik', address='Fortnite vej 23', age=69))
        data.append(Customer(name='Marcus', address='Omegavej 420', age=10))
        data.append(Customer(name='Hans', address='sejvej 1', age=200))
        data.append(Customer(name="John Smith", address="123 Main St.", age=30))
        data.append(Customer(name="Sarah Johnson", address="456 Elm St.", age=40))
        data.append(Customer(name="Mike Davis", address="789 Oak St.", age=50))
        data.append(Customer(name="Lisa Jones", address="101 Maple Ave.", age=45))
        data.append(Customer(name="David Lee", address="555 Pine St.", age=35))

        # Product data
        data.append(Product(product_number=1234, price=12.99, brand='Nike'))
        data.append(Product(product_number=5678, price=24.99, brand='Adidas'))
        data.append(Product(product_number=9101, price=9.99, brand='Puma'))
        data.append(Product(product_number=1213, price=39.99, brand='Under Armour'))
        data.append(Product(product_number=1415, price=19.99, brand='Reebok'))

        session.add_all(data)
        session.commit()

def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record

engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)



print(f"{select_all(Customer)}\n{select_all(Product)}")
print(get_record(Customer, 1))
print(get_record(Product, 3))
print(Customer())
print(Product())