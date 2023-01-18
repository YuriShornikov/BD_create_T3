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
            client_id INTEGER NOT NULL REFERENCES clients(id)
            );
        """)

        con.commit()

def add_clients(con, name, surname, email, phone):
    with con.cursor() as cur:
        cur.execute("""
            INSERT INTO clients(name, surname, email) 
            VALUES(%s, %s, %s);""",
            (name, surname, email, )
        )

        cur.execute("""
            INSERT INTO phones(phone, client_id)
            VALUES (%s);""",
            (name, phone, )
        )


if __name__ == '__main__':
    con = psycopg2.connect(database="sql_python", user="postgres", password="Irregularlypost")
    createdb(con)