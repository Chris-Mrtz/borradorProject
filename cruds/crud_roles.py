from .conexion_mysql import ConexionMySQL
conexion = ConexionMySQL()

def buscar_rol(nombre):
    try:
        sql = "SELECT * FROM roles WHERE nombre = %s"
        datos = (nombre,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error al buscar el rol: {e}")