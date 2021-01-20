import sqlite3
from sqlite3 import Error

from valores_cambio import get_valores


def create_table(conexion, create_table_sql):
    """ crea una tabla
    :param conexion: Objeto que trae la conexion
    :param create_table_sql: SQL
    :return:
    """
    try:
        c = conexion.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def guardar():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    valores = get_valores()
    if (valores):
        print("Tasas de cambio obtenidas")

    sql_tabla = """ CREATE TABLE IF NOT EXISTS valores (
                                                 id integer PRIMARY KEY,
                                                 fecha text NOT NULL,
                                                valor text NOT NULL); """
    create_table(conn, sql_tabla)
    cursor.execute("select  count(*) from valores")

    result = cursor.fetchone()
    if result[0] == 0:
        i = 1
        for key, value in valores.items():
            parametros = i, key, value['USD']
            sql = '''INSERT INTO valores(id,fecha,valor) VALUES (?,?,?)'''
            cursor.execute(sql, parametros)
            i = i + 1
        conn.commit()
    print("Datos grabados correctamente")
