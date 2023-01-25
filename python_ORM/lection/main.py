import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Course, Homework

#Data sourse name
#в кавычках перечисляются: имя:пароль@Путь (локальный):порт (5432 обычный)/ название базы данных
DSN = 'postgresql://postgres:Irregularlypost@localhost:5432/ORMp'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

#Создание сессии

Session = sessionmaker(bind=engine)

#Создаем экземляр нашего класса

session = Session()

course1 = Course(name='python')
print(course1.name)

session.add(course1)
session.commit()

print(course1.id)
print(course1)

home1 = Homework(number=1, description='write lecture', course=course1)
home2 = Homework(number=2, description='read lecture', course=course1)

session.add_all([home1, home2])
session.commit()
# print(home1)
# print(home2)

#поиск через цикл for
for c in session.query(Homework).filter(Homework.number > 1):
    print(c)

for t in session.query(Homework).filter(Homework.description.like('%read%')):
    print(t)

for j in session.query(Course).join(Homework.course).filter(Homework.number == 1).all():
    print(j)

#подзапрос
subq = session.query(Homework).filter(Homework.description.like('%wr%')).subquery()

#использование подзапроса
for c in session.query(Course).join(subq, Course.id == subq.c.course_id).all():
    print(c)

course2 = Course(name='Javascript')
session.add(course2)
session.commit()

session.query(Course).filter(Course.name == 'Javascript').update({'name': 'Java'})
session.commit()

session.query(Course).filter(Course.name == 'Java').delete()
session.commit()

for c in session.query(Course).all():
    print(c)


session.close()