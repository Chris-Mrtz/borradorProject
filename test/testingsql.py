from cruds.crud_usuarios import buscar_usuario, actualizar_contrasena
from utils.validar_contrasena import verificar_contrasena
from cruds.crud_empleado import ingresar_empleado, buscar_empleado
from cruds.crud_permisos import buscar_permiso_por_empleado

usuario_martinez = buscar_usuario(2)
contrasena = usuario_martinez[2]
contra = input()
print(verificar_contrasena(contra, contrasena))


