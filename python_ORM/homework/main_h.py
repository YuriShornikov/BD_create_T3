import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models_h import Publisher, Book, Stock, Shop, Sale

from DSN import DSN

engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)

session = Session()

