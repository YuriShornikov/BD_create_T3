import psycopg2

con = psycopg2.connect(database="sql_python", user="postgres", password="Irregularlypost")
with con.cursor() as cur:
    cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
    con.commit() # повторное создаине таблицы не произойдет, выдаст ошибку, комитит в конце
    con.rollback() #игнорит все изменения

con.close()