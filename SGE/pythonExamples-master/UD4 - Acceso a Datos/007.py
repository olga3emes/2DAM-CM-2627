import MySQLdb
def getConnection():
    db_host = 'localhost'
    usuario = 'root'
    clave = 'clave'
    base_de_datos = 'mi_basededatos'
    conn = MySQLdb.connect(host=db_host, user=usuario, passwd=clave, db=base_de_datos)
    return conn