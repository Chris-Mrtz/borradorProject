from cruds.crud_usuarios import insertar_usuario, buscar_usuario
from cruds.crud_empleado import ingresar_empleado


from .Personas import Personas

class Usuario(Personas):
    def __init__(self, username, password, salario, fecha_inicio, departamento, nombre, email, telefono, direccion, rol):
        super().__init__(nombre, email, telefono, direccion)
        self.username = username
        self.password = password
        self.salario = salario
        self.fecha_inicio = fecha_inicio
        self.departamento = departamento
        self.rol = rol

    def obtener_descripcion(self):
        pass

    def crear_usuario(self):

        ingresar_empleado(self.nombre, self.direccion, self.telefono, self.email, self.salario, self.rol, self.departamento,1, self.username, self.password)
        print("Usuario creado exitosamente")

    def obtener_id_usuario(self):
        id_usuario = buscar_usuario(self.nombre)
        print(id_usuario)
        resultado = id_usuario[0]
        return resultado

    def crear_empleado(self, id_rol, id_departamento, id_usuario):
        ingresar_empleado(self.nombre, self.direccion, self.telefono, self.email, self.salario, id_rol, id_departamento, id_usuario, self.username, self.password)
        print("El empleado creado exitosamente")

