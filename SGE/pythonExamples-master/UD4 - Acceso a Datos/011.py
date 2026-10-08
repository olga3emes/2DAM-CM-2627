import MySQLdb

def get_connection():
    """
    Establece y devuelve una conexión a la base de datos MySQL.
    """
    try:
        conn = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='',
            db='usuarios',
            charset='utf8mb4',
            autocommit=False  # Desactivamos autocommit para gestionar transacciones manualmente
        )
        return conn
    except MySQLdb.DatabaseError as e:
        print(f"[ERROR] Conexión fallida: {e}")
        return None

def insertar_usuario(nombre):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("START TRANSACTION")
            cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nombre,))
            conn.commit()
            print("✅ Usuario insertado correctamente.")
        except MySQLdb.DatabaseError as e:
            conn.rollback()
            print(f"[ERROR] Error al insertar usuario: {e}")
        finally:
            cursor.close()
            conn.close()

def buscar_usuario(nombre):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("START TRANSACTION READ ONLY")
            cursor.execute("SELECT id, nombre FROM usuarios WHERE nombre LIKE %s", (f"%{nombre}%",))
            resultados = cursor.fetchall()
            for fila in resultados:
                print(f"🔎 ID: {fila[0]}, Nombre: {fila[1]}")
            conn.commit()
        except MySQLdb.DatabaseError as e:
            conn.rollback()
            print(f"[ERROR] Error al buscar usuario: {e}")
        finally:
            cursor.close()
            conn.close()

def buscar_usuarios(limit=5, offset=0):
    """
    Recupera una lista paginada de usuarios desde la base de datos.
    Args:
        limit (int): Número de usuarios a mostrar (por página).
        offset (int): Desplazamiento desde el primer registro (para paginación).
    """
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("START TRANSACTION READ ONLY")
            cursor.execute("SELECT id, nombre FROM usuarios ORDER BY id ASC LIMIT %s OFFSET %s",(limit, offset) )
            resultados = cursor.fetchall()
            for fila in resultados:
                print(f"🔎 ID: {fila[0]}, Nombre: {fila[1]}")
            conn.commit()
        except MySQLdb.DatabaseError as e:
            conn.rollback()
            print(f"[ERROR] Error al obtener usuarios: {e}")
        finally:
            cursor.close()
            conn.close()

def actualizar_nombre_usuario(user_id, nuevo_nombre):
    """
    Actualiza el nombre de un usuario según su ID de forma segura.
    """
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("START TRANSACTION")
            cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (nuevo_nombre, user_id) )
            conn.commit()
            print("✏️ Nombre actualizado correctamente.")
        except MySQLdb.DatabaseError as e:
            conn.rollback()
            print(f"[ERROR] No se pudo actualizar el nombre: {e}")
        finally:
            cursor.close()
            conn.close()

def eliminar_usuario_por_id(user_id):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("START TRANSACTION")
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
            conn.commit()
            print("❌ Usuario eliminado correctamente.")
        except MySQLdb.DatabaseError as e:
            conn.rollback()
            print(f"[ERROR] No se pudo eliminar el usuario: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    #Primero ejecutar el fichero usuarios.sql
    buscar_usuario("Olg")
    actualizar_nombre_usuario(1,"Olga M.")
    eliminar_usuario_por_id(1)
    buscar_usuario("Olg")
    insertar_usuario("Carlos")
    buscar_usuario("Carlos")
    insertar_usuario("Juan Carlos")
    insertar_usuario("Javier")
    insertar_usuario("Soraya")
    insertar_usuario("Pablo")
    insertar_usuario("Paula")
    insertar_usuario("Olga")
    # Página 1 → primeros 5 usuarios
    buscar_usuarios(limit=5, offset=0)
    # 💡TRUCO: el offset se puede calcular como limit*(num_pagina -1)
    # Página 2 → siguientes 5 usuarios
    #buscar_usuarios(limit=5, offset=5)
