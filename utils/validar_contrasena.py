import bcrypt

def hashear_contrasena(contrasena):
    #Generar un salt aleatorio
    sal = bcrypt.gensalt()
    #Hashear la contrasena con salt y condificarla
    contrasena_hash = bcrypt.hashpw(contrasena.encode('utf-8'), sal)
    return contrasena_hash.decode('utf-8')

def verificar_contrasena(contrasena_ingresada, contrasena_almacenada):
    return bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), contrasena_almacenada.encode('utf-8'))