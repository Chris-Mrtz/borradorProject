from .conexion_mysql import ConexionMySQL
conexion = ConexionMySQL()

def ingresar_proyecto(nombre, descripcion):
    try:
        sql = "INSERT INTO proyectos(nombre, descripcion) VALUES (%s, %s)"
        datos = (nombre, descripcion)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al ingresar el proyecto: {e}")
        conexion.conexion.rollback()

def buscar_proyecto(nombre):
    try:
        sql = "SELECT * FROM proyectos WHERE nombre = %s"
        datos = (nombre,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error buscando el proyecto: {e}")

def eliminar_proyecto(id):
    try:
        sql = "DELETE FROM proyectos WHERE id = %s"
        datos = (id,)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error eliminar el proyecto: {e}")
        conexion.conexion.rollback()


def asignar_proyecto(id_empleado, id_proyecto):
    try:
        sql = "INSERT INTO asignacion_proyecto(id_empleado, id_proyecto) VALUES (%s, %s)"
        datos = (id_empleado, id_proyecto)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al asignar el proyecto: {e}")
        conexion.conexion.rollback()

def desasignar_proyecto(id_empleado, id_proyecto):
    try:
        sql = "DELETE FROM asignacion_proyecto WHERE id_empleado = %s AND id_proyecto = %s"
        datos = (id_empleado, id_proyecto)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al desasignar el proyecto: {e}")
        conexion.conexion.rollback()
