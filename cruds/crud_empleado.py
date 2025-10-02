from .conexion_mysql import ConexionMySQL
conexion = ConexionMySQL()

def ingresar_empleado(nombre, direccion, numeroTel, correo, salario, id_rol, id_departamento, id_usuario):
    try:
        sql = ("INSERT INTO empleados(nombre, direccion, telefono, email, salario, id_rol, id_departamento, "
               "id_usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        datos = (nombre, direccion, numeroTel, correo, salario, id_rol,id_departamento, id_usuario)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al insertar el empleado: {e}")
        conexion.conexion.rollback()

def editar_empleado( nombre, direccion, numeroTel, correo, salario, id_rol, id_departamento, id_usuario, id):
    try:
        sql = ("UPDATE empleados SET nombre = %s "
               "set direccion = %s "
               "set numero_de_telefono = %s "
               "set correo = %s "
               "set salario = %s "
               "set id_rol = %s "
               "set id_departamento = %s "
               "set id_usuario = %s WHERE id = %s")
        datos = (nombre, direccion, numeroTel, correo, salario, id_rol, id_departamento, id_usuario, id)
        conexion.cursor.execute(sql, datos)
        conexion.connection.commit()
    except Exception as e:
        print(f"Error al actualizar el empleado: {e}")
        conexion.conexion.rollback()

def buscar_empleado(id_empleado):
    try:
        sql = "SELECT * FROM empleados WHERE id_empleado = %s"
        datos = (id_empleado,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error al buscar el empleado: {e}")