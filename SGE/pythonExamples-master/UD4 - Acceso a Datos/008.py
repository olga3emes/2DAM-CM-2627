import MySQLdb
import logging
#logging es para generar logs - Buena práctica
def get_connection():
    """
    Establece una conexión con la base de datos MySQL.
    Returns:
        conn (MySQLdb.connections.Connection): Objeto de conexión a la base de datos.
    Raises:
        MySQLdb.DatabaseError: Si hay un error en la conexión.
    """
    try:
        conn = MySQLdb.connect(
            host='localhost',
            user='usuario',
            passwd='',
            db='mi_basededatos',
            charset='utf8mb4'
        )
        print('Connection established')
        return conn
    except MySQLdb.DatabaseError as e:
        #También podemos usar Error como clase general
        logging.error(f"Error al conectar con la base de datos: {e}")
        raise

get_connection()


