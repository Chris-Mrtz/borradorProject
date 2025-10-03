from abc import ABC, abstractmethod

class Personas(ABC):
    nombre: str
    email: str
    telefono: str
    direccion: str

    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion


    @abstractmethod
    def obtener_descripcion(self):
        datos_usuario = [self.nombre, self.email, self.telefono, self.direccion]
        return datos_usuario
