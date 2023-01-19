# import psycopg2
#
# con = psycopg2.connect(database="sql_python", user="postgres", password="Irregularlypost")
# with con.cursor() as cur:
#     cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
#     con.commit() # повторное создаине таблицы не произойдет, выдаст ошибку, комитит в конце
#     con.rollback() #игнорит все изменения
#
#
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS genre
#         genre_id SERIAL PRIMARY KEY
#         name VARCHAR(60) NOT NULL
#         """)
#
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS musician
#         musician_id SERIAL PRIMARY KEY
#         name VARCHAR(60)
#         """)
#
#     cur.execute("""
#         CREATE TABLE MUSICIAN_genre
#         id SERIAL PRIMARY KEY
#         genre_id SERIAL NOT NULL references genre(genre_id)
#         musician_id SERIAL NOT NULL references musician(musician_id)
#         """)
#
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS album
#         album_id SERIAL PRIMARY KEY
#         name VARCHAR(60) NOT NULL
#         """)
#
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS musician_album
#         id SERIAL PRIMARY KEY
#         musician_id SERIAL NOT NULL references musician(musician_id)
#         album_id SERIAL NOY NULL references album(album_id
#         """)
#
#     cur.execute("""
#             CREATE TABLE IF NOT EXISTS """)
#
#
# con.close()

import psycopg2




def createdb(con):
    with con.cursor() as cur:

        cur.execute("""
        DROP TABLE phones;
        DROP TABLE clients;
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            name VARCHAR(60) NOT NULL,
            surname VARCHAR(60) NOT NULL,
            email VARCHAR NOT NULL
            );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phones(
            id SERIAL PRIMARY KEY,
            phone VARCHAR,
            client_id SERIAL NOT NULL REFERENCES clients(id)
            );
        """)

        con.commit()

def add_clients(con, name, surname, email, phone=None):
    with con.cursor() as cur:
        cur.execute("""
            INSERT INTO clients(name, surname, email) 
            VALUES(%s, %s, %s);""",
            (name, surname, email, )
        )

        cur.execute("""
            INSERT INTO phones(phone)
            VALUES (%s);""",
            (phone, )
        )

        con.commit()

def add_phone(con, client_id, phone):
    with con.cursor() as cur:
        cur.execute("""
            INSERT INTO phones(client_id, phone)
            VALUES (%s , %s);""",
            (client_id, phone, )
        )

        con.commit()

def update_client(con, client_id, name, surname, email, phone):
    with con.cursor() as cur:
        cur.execute("""
            UPDATE clients SET name = %s, surname = %s, email = %s
            WHERE id = %s;""",
            (name, surname, email, client_id, )
        )

        cur.execute("""
            UPDATE phones SET phone = %s
            WHERE client_id = %s;""",
            (phone, client_id, )
        )

if __name__ == '__main__':
    con = psycopg2.connect(database="sql_python", user="postgres", password="Irregularlypost")
    createdb(con)
    add_clients(con, name="test", surname="test", email="test@gmail.com", phone=" ")
    add_phone(con, client_id=1, phone=99999)
    update_client(con, client_id=1, name="test2", surname="test2", email="test2@gmail.com", phone=11111)