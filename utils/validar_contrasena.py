import bcrypt

def verificar_contrasena(contrasena_ingresada, contrasena_almacenada):
    return bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), contrasena_almacenada.encode('utf-8'))