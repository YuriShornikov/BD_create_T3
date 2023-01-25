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

#вопрос
def search_client(con, position):
    with con.cursor() as cur:
        # cur.execute("""
        #     select
        #     case
        #         when id = (
    	#         SELECT p.client_id FROM phones p
    	#         JOIN clients c ON p.client_id = c.id
    	#         WHERE p.phone = %s)
    	#             then c.id
    	#         when c.name = %s
    	#             then c.id
    	#         when c.surname = %s
    	#             then c.id
    	#         when c.email = %s
    	#             then c.id
    	#     end as client_id from clients c;""",
        #     (position, )
        # )
        # return cur.fetchall()[0]





        # cur.execute("""
        #     SELECT id FROM clients c
        #     WHERE c.id = (
        #         SELECT p.client_id FROM phones p
        #         JOIN clients c ON p.client_id = c.id
        #         WHERE p.phone = %s) or name = %s or surname = %s or email = %s;""",
        #     (position, )
        # )

        cur.execute("""
            SELECT id FROM clients c
            WHERE c.id = (
                SELECT p.client_id FROM phones p
                JOIN clients c ON p.client_id = c.id
                WHERE p.phone = %s);""",
            (position,)
        )
        result = cur.fetchall()
        if len(result) > 0:
            print(result)

        cur.execute("""
            SELECT id FROM clients c
            WHERE c.name = %s;""",
            (position, )
        )
        result = cur.fetchall()
        if len(result) > 0:
            print(result)

        cur.execute("""
            SELECT id FROM clients c
            WHERE c.surname = %s;""",
            (position,)
        )
        result = cur.fetchall()
        if len(result) > 0:
            print(result)

        cur.execute("""
            SELECT id FROM clients c
            WHERE c.email = %s;""",
            (position,)
        )
        result = cur.fetchall()
        if len(result) > 0:
            print(result)


        con.commit()

if __name__ == '__main__':
    con = psycopg2.connect(database="sql_python", user="postgres", password="Irregularlypost")
    # createdb(con)
    # add_clients(con, name="test", surname="test", email="test@gmail.com", phone="77777") #добавляет клиента
    # add_phone(con, client_id=1, phone="99999") #добавляет телефон
    # # update_client(con, client_id=1, name="test2", surname="test2", email="test2@gmail.com", phone="11111")
    # # delete_phone(con, name="test2", phone="11111")
    # # delete_client(con, name="test2")
    search_client(con, position="test2@gmail.com")