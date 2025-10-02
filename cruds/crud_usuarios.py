from .conexion_mysql import  ConexionMySQL
import bcrypt

conexion = ConexionMySQL()

def hashear_contrasena(contrasena):
    #Generar un salt aleatorio
    sal = bcrypt.gensalt()
    #Hashear la contrasena con salt y condificarla
    contrasena_hash = bcrypt.hashpw(contrasena.encode('utf-8'), sal)
    return contrasena_hash.decode('utf-8')


def insertar_usuario(usuario, contrasena):
    try:
        contrasena_segura = hashear_contrasena(contrasena)
        sql = 'INSERT INTO usuarios(usuario, contrasena) VALUES (%s, %s)'
        datos = (usuario, contrasena_segura)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()

    except Exception as e:
        print(f"Error al insertar usuario: {e}")
        conexion.conexion.rollback()


def actualizar_contrasena(id, contrasena):
    try:
        contrasena_segura = hashear_contrasena(contrasena)
        sql = "UPDATE usuarios SET contrasena = %s WHERE id = %s"
        datos = (contrasena_segura, id)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error actualizando la contrasena: {e}")
        conexion.conexion.rollback()

def buscar_usuario(id):
    try:
        sql = "SELECT * FROM usuarios WHERE id = %s"
        datos = (id,)
        conexion.cursor.execute(sql, datos)
        resultado = conexion.cursor.fetchone()
        return resultado
    except Exception as e:
        print(f"Error al buscar el usuario: {e}")

def eliminar_usuario(id):
    try:
        sql = "DELETE FROM usuarios WHERE id = %s"
        datos = (id,)
        conexion.cursor.execute(sql, datos)
        conexion.conexion.commit()
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
        conexion.conexion.rollback()



