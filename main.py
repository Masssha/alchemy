import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock

DSN = "postgresql://postgres:LLllMMmmqwerty654321@localhost:5432/users"

engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

book_1 = Book(title="Little pizza")
publisher_1 = Publisher(name="Misha")
shop_1 = Shop(name="biblio")

session.add(publisher_1)
session.add(book_1)
session.commit()

session.close()

