import psycopg2

con = psycopg2.connect(database="sql_python", user="postgres", password="Irregularlypost")
with con.cursor() as cur:
    cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
    con.commit() # повторное создаине таблицы не произойдет, выдаст ошибку, комитит в конце
    con.rollback() #игнорит все изменения


    cur.execute("""
        CREATE TABLE IF NOT EXISTS genre
        genre_id SERIAL PRIMARY KEY
        name VARCHAR(60) NOT NULL
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS musician
        musician_id SERIAL PRIMARY KEY
        name VARCHAR(60)
        """)

    cur.execute("""
        CREATE TABLE MUSICIAN_genre
        id SERIAL PRIMARY KEY
        genre_id SERIAL NOT NULL references genre(genre_id)
        musician_id SERIAL NOT NULL references musician(musician_id)
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS album
        album_id SERIAL PRIMARY KEY
        name VARCHAR(60) NOT NULL
        """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS musician_album
        id SERIAL PRIMARY KEY
        musician_id SERIAL NOT NULL references musician(musician_id)
        album_id SERIAL NOY NULL references album(album_id
        """)

    cur.execute("""
            CREATE TABLE IF NOT EXISTS """)


con.close()