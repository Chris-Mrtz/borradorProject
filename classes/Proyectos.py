from cruds.crud_proyectos import ingresar_proyecto, actualizar_proyecto, eliminar_proyecto, buscar_los_proyectos, buscar_proyecto


class Proyectos:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio


    def ingresar_nuevo_proyecto(self):
        ingresar_proyecto(self.nombre, self.descripcion)

    def editar_proyecto(self, nombre, descripcion, id_proyecto):
        actualizar_proyecto(id_proyecto, nombre, descripcion)

    def eliminar_proyecto(self, id_proyecto):
        eliminar_proyecto(id_proyecto)

    def buscar_todos_los_proyectos(self):
        buscar_los_proyectos()

    def buscar_proyecto(self):
        buscar_proyecto(self.nombre)




