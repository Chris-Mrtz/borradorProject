from .conexion_mysql import ConexionMySQL
conexion = ConexionMySQL()

def buscar_rol(id):
    try:
        sql = "SELECT * FROM rol WHERE id = %s"
        datos = (id,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error al buscar el rol: {e}")

def buscar_roles():
    try:
        sql = "SELECT nombre FROM rol"
        conexion.cursor.execute(sql)
        resultado = conexion.cursor.fetchall()
        return resultado
    except Exception as e:
        print(f"Error al buscar el roles: {e}")