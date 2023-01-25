import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models_h import Publisher, Book, Stock, Shop, Sale

from DSN import DSN

engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)

session = Session()

publisher1 = Publisher(name="Пушкин")
book1 = Book(title="Капитанская дочка", id_publisher=1)
shop1 = Shop(name="Буквоед")
sale1 = Sale(price=500, date_sale="")
book2 = Book(title="Руслан и Людмила", id_publisher=1)
shop2 = Shop(name="Буквоед")
book3 = Book(title="Капитанская дочка", id_publisher=1)
shop3 = Shop(name="Лабиринт")
book4 = Book(title="Евгений Онегин", id_publisher=1)
shop4 = Shop(name="Книжный дом")
book5 = Book(title="Капитанская дочка", id_publisher=1)
shop5 = Shop(name="Буквоед")
session.add(publisher1)
session.commit()



