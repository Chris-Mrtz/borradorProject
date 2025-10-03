from cruds.crud_departamentos import buscar_departamento, asignar_gerente_a_departamento

class Departamentos:

    def __init__(self, nombre, descripcion, gerente):
        self.nombre = nombre
        self.descripcion = descripcion
        self.gerente = gerente


    def obtener_id_departamento(self):
        departamento_a_buscar = buscar_departamento(self.nombre)
        id_departamento = departamento_a_buscar[0]
        return id_departamento

    def asignar_departamento(self, id_departamento, id_empleado):
        try:
            asignar_gerente_a_departamento(id_departamento, id_empleado)
        except Exception as e:
            print(f"Error al asignar de departamento: {e}")








