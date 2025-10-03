from classes.Usuarios import Usuario
from classes.Roles import Roles

rol_admin = Roles('admin').obtener_rol()

cristian = Usuario('vlabra', 'vicente', 500000, '02-10-2025', 'RRHH', 'Vicente', 'vlabra@gmail.com', '8095992210', 'Esquina Gutierrez 2025', rol_admin)
cristian.imprimir_rol()
#cristian.crear_usuario()



