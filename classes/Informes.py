from cruds.crud_usuarios import buscar_usuario
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
from typing import Optional, Any, Dict, Union
from pathlib import Path
import pandas as pd

class Informes:
    def __init__(self, nombre_proyecto: str, tipo: str, fecha_generacion: Optional[datetime] = None, generado_por: Optional[Any] = None):
        self.nombre_proyecto = nombre_proyecto
        self.tipo = tipo
        self.fecha_generacion = fecha_generacion or datetime.now()
        self.username = None
        self.departamento = None
        self.resolver_usuario(generado_por)

    def resolver_usuario(self, generado_por: Any) -> None:

        if isinstance(generado_por, str):
            usuario = buscar_usuario(generado_por)
            if usuario:
                self.username = usuario.get('username')
                self.departamento = usuario.get('departamento')
                resultado = buscar_usuario(generado_por)
            else:
                self.username = generado_por
                self.departamento = "Desconocido"
        else:
            self.username = getattr(generado_por, 'username', 'Desconocido')
            self.departamento = getattr(generado_por, 'departamento', 'Desconocido')


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

