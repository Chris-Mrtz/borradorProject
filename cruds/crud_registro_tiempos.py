from .conexion_mysql import ConexionMySQL
conxion = ConexionMySQL()

def ingresar_registro_de_tiempo(fecha, cantidadDeHoras, descripcion, id_empleado, id_proyecto):
    try:
        sql = "INSERT INTO regisro_tiempos (fecha, cantidad_de_horas, descripcion, id_empleado, id_proyecto) VALUES (%s, %s, %s, %s, %s)"
        datos = (fecha, cantidadDeHoras, descripcion, id_empleado, id_proyecto)
        conxion.cursor.execute(sql, datos)
        conxion.conexion.commit()
    except Exception as e:
        print(f"Error al actualizar registro tiempo: {e}")
        conxion.conexion.rollback()


