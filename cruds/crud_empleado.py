from .conexion_mysql import ConexionMySQL
from utils.validar_contrasena import hashear_contrasena
conexion = ConexionMySQL()

def ingresar_empleado(nombre, direccion, numeroTel, correo, salario, id_rol, id_departamento, id_usuario, usuario, contrasena):
    try:
        contrasena_segura = hashear_contrasena(contrasena)
        sql = ("INSERT INTO empleados(nombre, direccion, telefono, email, salario, id_rol, id_departamento, "
               "id_usuario, usuario, contrasena) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        datos = (nombre, direccion, numeroTel, correo, salario, id_rol,id_departamento, id_usuario, usuario, contrasena_segura)
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

def buscar_empleado_por_usuario(id_usuario):
    try:
        sql = "SELECT * FROM empleados WHERE id_usuario = %s"
        datos = (id_usuario,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error al buscar el empleado: {e}")

def buscar_informacion_de_los_empleados():
    try:
        sql = "SELECT empleados.id_empleado, empleados.nombre, rol.nombre, departamentos.nombre, empleados.email FROM empleados INNER JOIN rol ON empleados.id_rol = rol.id INNER JOIN departamentos ON empleados.id_departamento = departamentos.id_depto "

        conexion.cursor.execute(sql)
        resultado = conexion.cursor.fetchall()
        return resultado
    except Exception as e:
      print(f"Error al buscar los empleados: {e}")
