import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables

#Data sourse name
#в кавычках перечисляются: имя:пароль@Путь (локальный):порт (5432 обычный)/ название базы данных
DSN = 'postgresql://postgres:Irregularlypost@Localhost:5432/ORMp'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

#Создание сессии

Session = sessionmaker(bind=engine)

#Создаем экземляр нашего класса

session = Session()

session.close()