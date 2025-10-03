from .conexion_mysql import ConexionMySQL
conexion = ConexionMySQL()

def ingresar_departamento(nombre, descripcion, id_empleado):
    try:
        sql = 'INSERT INTO departamentos (nombre, descripcion, gerente) VALUES (%s, %s, %s)'
        datos = (nombre, descripcion, id_empleado)
        conexion.cursor.execute(sql, datos)
        conexion.connection.commit()
    except Exception as e:
        print(f"Error al insertar departamento: {e}")
        conexion.conexion.rollback()

def buscar_departamento(nombre):
    try:
        sql = 'SELECT * FROM departamentos WHERE nombre = %s'
        datos = (nombre,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error al buscar departamento: {e}")

def buscar_todos_los_departamentos():
    try:
        sql = 'SELECT nombre FROM departamentos'
        conexion.cursor.execute(sql)
        resultado = conexion.cursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Error al buscar todos los departamentos: {e}")

def editar_departamento(nombre, descripcion, id_empleado, id):
    try:
        sql = ("UPDATE departamentos set nombre = %s "
               "set descripcion = %s "
               "set id_empleado = %s "
               "where id = %s")
        datos = (nombre, descripcion, id_empleado, id)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al editar departamento: {e}")
        conexion.conexion.rollback()

def eliminar_departamento(id):
    try:
        sql = "DELETE FROM departamentos WHERE id = %s"
        datos = (id,)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()

    except Exception as e:
        print(f"Error al eliminar departamento: {e}")
        conexion.conexion.rollback()

def asignar_gerente_a_departamento(id_departamento, id_empleado):
    try:
        sql = "INSERT INTO asignacion_gerente(id_departamento, id_empleado) VALUES (%s, %s)"
        datos = (id_departamento, id_empleado)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al asignar de departamento: {e}")
        conexion.conexion.rollback()