# baza danych
# baza SQL lite w pythone

import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect('baza.db')
    cursos = sql_connection.cursor()
    print("Baza danych została podłączona")
    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAT NOT NULL);
    """
    cursos.execute(query)
    sql_connection.commit()
    insert = """
    INSERT INTO developers (id,name,email,salary) VALUES (1, 'Radek','radel@radel.pl',10000)
    """
    # cursos.execute(insert)
    # sql_connection.commit()

    select = """
    SELECT * FROM developers;"""

    for row in cursos.execute(select):
        print(row)
        

except sqlite3.Error as e:
    print("Błąd", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
