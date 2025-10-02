from .conexion_mysql import ConexionMySQL

conexion = ConexionMySQL()

def insertar_modulos(nombre, descripcion):
    try:
        sql = "INSERT INTO modulos(nombre, descripcion) VALUES (%s, %s)"
        datos = (nombre, descripcion)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al ingresar el modulo: {e}")
        conexion.conexion.rollback()

def editar_modulo(id, nombre, descripcion):
    try:
        sql = "UPDATE modulos SET nombre = %s, descripcion = %s WHERE id = %s"
        datos = (nombre, descripcion, id)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al actualizar el modulo: {e}")
        conexion.conexion.rollback()

def buscar_modulo (id):
    try:
        sql = "SELECT * FROM modulos WHERE id = %s"
        datos = (id,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado

    except Exception as e:
        print(f"Error buscando el modulo: {e}")
