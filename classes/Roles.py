from cruds.crud_roles import buscar_roles, buscar_rol

class Roles:
    def __init__(self, rol):
        self.rol = rol


    def obtener_rol(self):
        return buscar_rol(self.rol)

    def obtener_todos_los_roles(self):
        return buscar_roles()




