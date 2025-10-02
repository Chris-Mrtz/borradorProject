from .conexion_mysql import ConexionMySQL
conexion = ConexionMySQL()

def agregar_permiso(id_rol, id_modulo):
    try:
        sql = 'INSERT INTO permisos(id_rol, id_modulo) VALUES (%s, %s)'
        datos = (id_rol, id_modulo)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error otorgando el permiso: {e}")
        conexion.conexion.rollback()

def remover_permiso(id_rol, id_modulo):
    try:
        sql = "DELETE FROM permisos WHERE id_rol = %s AND id_modulo = %s"
        datos = (id_rol, id_modulo)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f'Error al eliminar el permiso: {e}')
        conexion.conexion.rollback()

def buscar_permisos(id_rol):
    try:
        sql = "SELECT * FROM permisos WHERE id_rol = %s"
        datos = (id_rol)
        conexion.cursor.execute(sql, datos)

    except Exception as e:
        print(f"Error buscando los permisos: {e}")

def buscar_permiso_por_empleado(id_empleado):
    try:
        sql = (
            "SELECT * FROM empleados "
            "INNER JOIN rol ON empleados.id_rol = rol.id "
            "INNER JOIN permisos ON empleados.id_rol = permisos.id_rol "
            "INNER JOIN modulos ON permisos.id_modulo = modulos.id "
            "WHERE empleados.id_empleado = %s"
        )
        datos = (id_empleado,)
        conexion.cursor.execute(sql, datos)
        permiso_por_empleado = conexion.cursor.fetchall()
        return permiso_por_empleado
    except Exception as e:
        print(f"Error al buscar el permiso por el empleado: {e}")