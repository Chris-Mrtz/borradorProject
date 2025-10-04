from cruds.crud_usuarios import buscar_usuario
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pandas as pd
from datetime import datetime
from typing import Optional, Any, Dict, Union
from pathlib import Path

class Informes:
    def __init__(self, nombre_proyecto: str, tipo: str, fecha_generacion: Optional[datetime] = None, generado_por: Optional[Any] = None):
        self.nombre_proyecto = nombre_proyecto
        self.tipo = tipo
        self.fecha_generacion = fecha_generacion or datetime.now()

        
        self.resolver_usuario(generado_por)

    def resolver_usuario(self, generado_por: Any) -> None:
        usuario_obj = None

        if isinstance(generado_por, str):
            try:
                resultado = buscar_usuario(generado_por)
                if resultado:
                    #si es tupla/lista, toma username y departamento
                    if isinstance(resultado, (tuple, list)):
                        username =  resultado[1] if len(resultado) > 1 else generado_por
                        departamento = resultado[2] if len(resultado) > 2 else "N/A"
                        usuario_obj = type("Usuario", (), {
                            "username": username,
                            "departamento": departamento
                        })()
                    else:
                        usuario_obj = resultado
            except Exception as e:
                print(f"Error al buscar usuario: {e}")
                usuario_obj = type("Usuario", (), {
                    "username": generado_por,
                    "departamento": "N/A"
                })()
        elif generado_por is None:
            usuario_obj = type("Usuario", (), {
                "username": "Desconocido",
                "departamento": "N/A"
            })()
        else:
            usuario_obj = generado_por

        self.generado_por = usuario_obj
        self.departamento = getattr(usuario_obj, "departamento", "N/A")
        self.username = getattr(usuario_obj, "username", "Sistema")


    def generar_informe_pdf(self, datos: Dict, ruta_salida: str) -> bool:
        try:
            c = canvas.Canvas(ruta_salida, pagesize=letter)
            width, height = letter

            #encabezado
            c.setFont("Helvetica-Bold", 16)
            c.drawString(50, height - 50, f"Informe de Proyecto: {self.nombre_proyecto}")

            #informacion general
            c.setFont("Helvetica", 12)
            c.drawString(50, height - 80, f"Fecha: {self.fecha_generacion.strftime('%d/%m/%Y %H:%M:%S')}")
            c.drawString(50, height - 100, f"Tipo: {self.tipo}")
            c.drawString(50, height - 120, f"Departamento: {self.departamento}")
            c.drawString(50, height - 140, f"Generado por: {self.username}")

            #contenido
            y_pos = height - 180
            for clave, valor in datos.items():
                if y_pos < 50:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_pos = height - 50
                
                c.drawString(50, y_pos, f"{clave}: {str(valor)}")
                y_pos -= 20
            
            c.save()
            return True
        except Exception as e:
            print(f"Error al generar el informe PDF: {e}")
            return False
    
    def generar_informe_excel(self, datos: Union[pd.DataFrame, Dict], ruta_salida: str) -> bool:
        try:
            if isinstance(datos, dict):
                df = pd.DataFrame([datos])
            else:
                df = datos

            #metadatos del informe
            metadata = pd.DataFrame([{
                'Nombre Proyecto': self.nombre_proyecto,
                'Tipo': self.tipo,
                'Fecha:': self.fecha_generacion.strftime('%d/%m/%Y %H:%M:%S'),
                'Generado por': self.username,
                'Departamento': self.departamento
            }])

            with pd.ExcelWriter(ruta_salida) as writer:
                metadata.to_excel(writer, sheet_name='Metadata', index=False)
                df.to_excel(writer, sheet_name='Datos', index=False)
            
            return True
        except Exception as e:
            print(f"Error al generar el informe Excel: {e}")
            return False

informe = Informes(
    nombre_proyecto="Proyecto X",
    tipo="Resumen",
    generado_por="admin_user"
)

datos_informe = {
    "Tarea 1": "Completada",
    "Tarea 2": "En progreso",
    "Tarea 3": "Pendiente"
}
informe.generar_informe_pdf(datos_informe, "informe_proyecto_x.pdf")

df_datos = pd.DataFrame(datos_informe.items(), columns=["Tarea", "Estado"])
informe.generar_informe_excel(df_datos, "informe_proyecto_x.xlsx")
