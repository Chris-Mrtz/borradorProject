import tkinter as tk
from tkinter import ttk, messagebox
from cruds.crud_empleado import buscar_informacion_de_los_empleados
from employee_form import EmployeeForm


class AdminDashboard(ttk.Frame):

    def __init__(self, master, db_manager=None):
        super().__init__(master)
        # Inicialización de atributos para evitar errores si no se establecen en otras funciones
        self.empleados_tree = None
        self.reporte_var = None
        self.content_frame = None

        self.master = master
        self.db = db_manager
        self.pack(expand=True, fill='both')
        self.current_view = None

        self.configurar_estilo()
        self.crear_diseno()
        self.mostrar_vista("Gestionar Usuarios")  # Muestra la vista de gestión de usuarios como inicio

    def configurar_estilo(self):
        """Configura el tema y los estilos personalizados de la aplicación."""
        style = ttk.Style()
        style.theme_use('clam')  # Un tema más moderno que el default

        # Color primario de EcoTech Solutions (verde)
        PRIMARY_COLOR = '#48BB78'
        DARK_BG_COLOR = '#2D3748'
        LIGHT_BG_COLOR = '#EDF2F7'

        # Estilo general para el fondo del dashboard
        style.configure('Dashboard.TFrame', background=LIGHT_BG_COLOR)
        self.config(style='Dashboard.TFrame')

        # Estilos para el menú lateral
        style.configure('Menu.TFrame', background=DARK_BG_COLOR)
        style.configure('Menu.TButton',
                        font=('Helvetica', 11, 'bold'),
                        background=DARK_BG_COLOR,
                        foreground='white',
                        padding=[15, 10])  # Aumentamos el padding para un mejor target táctil
        style.map('Menu.TButton',
                  background=[('active', PRIMARY_COLOR), ('pressed', PRIMARY_COLOR)],
                  foreground=[('active', DARK_BG_COLOR)])  # Texto oscuro al estar activo

        # Estilo para botones de acción (CRUD)
        style.configure('Action.TButton',
                        font=('Helvetica', 10, 'bold'),
                        padding=8,
                        background=PRIMARY_COLOR,
                        foreground='white')
        style.map('Action.TButton', background=[('active', '#38A169')])  # Tono más oscuro al pasar el ratón

        # Estilo para Treeview (Mejor lectura)
        style.configure('Treeview.Heading', font=('Helvetica', 10, 'bold'), background=PRIMARY_COLOR,
                        foreground='white')
        style.configure('Treeview', font=('Helvetica', 10), rowheight=25)

    def crear_diseno(self):
        # 1. Menú Lateral
        menu_frame = ttk.Frame(self, width=220, style='Menu.TFrame')
        menu_frame.pack(side='left', fill='y', padx=0, pady=0)

        # Título del Menú
        ttk.Label(menu_frame, text="EcoTech SGE", font=("Helvetica", 18, "bold"),
                  foreground='#48BB78', background='#2D3748').pack(pady=(20, 10), fill='x', padx=10)

        botones = [
            ("👤 Gestión de Usuarios", "Gestionar Usuarios"),
            ("🏢 Gestión de Departamentos", "Gestionar Departamentos"),
            ("🚀 Gestión de Proyectos", "Gestionar Proyectos"),
            ("⏱️ Registro de Tiempo", "Gestionar Tiempos"),
            ("📊 Generación de Informes", "Generar Informes")
        ]

        btn_container = ttk.Frame(menu_frame, padding=5, style='Menu.TFrame')
        btn_container.pack(fill='both', expand=True)

        for texto, vista in botones:
            btn = ttk.Button(btn_container, text=texto, style='Menu.TButton',
                             command=lambda v=vista: self.mostrar_vista(v))
            btn.pack(fill='x', padx=5, pady=5)

        # 2. Área de Contenido Principal
        self.content_frame = ttk.Frame(self, padding="30", style='Dashboard.TFrame')
        self.content_frame.pack(side='right', fill='both', expand=True)

    def limpiar_contenido(self):
        """Elimina todos los widgets del área de contenido."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def mostrar_vista(self, vista: str):
        """Carga el widget correspondiente a la vista seleccionada."""
        self.limpiar_contenido()

        # Título de la vista actual
        ttk.Label(self.content_frame, text=vista, font=("Helvetica", 20, "bold"),
                  foreground='#2D3748').pack(pady=(0, 25), anchor='w')

        if vista == "Gestionar Usuarios":
            self.crear_panel_gestion_usuarios()

        elif vista == "Gestionar Departamentos":
            self.crear_panel_generico(
                "Listado de Departamentos",
                ["ID", "Nombre", "Gerente ID", "Teléfono"],
                [
                    (1, "Desarrollo Sostenible", 1, "555-0101"),
                    (2, "Investigación y Desarrollo", 2, "555-0202"),
                    (3, "Ventas", 4, "555-0303"),
                ],
                'Departamento'
            )

        elif vista == "Gestionar Proyectos":
            self.crear_panel_generico(
                "Proyectos Activos",
                ["ID", "Nombre Proyecto", "Fecha Inicio", "Estado", "Líder ID"],
                [
                    (101, "Planta Solar Modular", "2024-01-01", "Activo", 1),
                    (102, "Filtros de Agua Biológicos", "2024-03-20", "En Pausa", 3),
                    (103, "Optimización de Residuos", "2024-09-15", "Activo", 5),
                ],
                'Proyecto'
            )

        elif vista == "Gestionar Tiempos":
            self.crear_panel_tiempo()

        elif vista == "Generar Informes":
            self.crear_panel_informes()

    def crear_panel_tiempo(self):
        """Panel para la gestión y aprobación de Registros de Tiempo."""
        ttk.Label(self.content_frame, text="Registros de Horas y Aprobación", font=("Helvetica", 14, 'bold')).pack(
            pady=10, anchor='w')

        info_frame = ttk.Frame(self.content_frame, padding="15", borderwidth=1, relief="solid")
        info_frame.pack(fill='x', pady=10)

        ttk.Label(info_frame,
                  text="Aquí se listarán los registros de tiempo de todos los empleados. El administrador podrá revisarlos y aprobarlos, implementando la lógica de negocio y validación de horas (Clase RegistroTiempo).",
                  wraplength=700).pack(pady=5)

        ttk.Button(self.content_frame, text="📈 Ver Resumen de Horas", style='Action.TButton').pack(pady=15,
                                                                                                   anchor='w')

    def crear_panel_informes(self):
        """Panel para la generación de informes."""
        ttk.Label(self.content_frame, text="Exportación de Datos", font=("Helvetica", 14, 'bold')).pack(pady=10,
                                                                                                        anchor='w')

        reportes_frame = ttk.Frame(self.content_frame, padding="15")
        reportes_frame.pack(fill='x', pady=10)

        ttk.Label(reportes_frame, text="Selecciona el tipo de informe:", font=('Helvetica', 10, 'bold')).grid(row=0,
                                                                                                              column=0,
                                                                                                              sticky='w',
                                                                                                              padx=10,
                                                                                                              pady=5)

        opciones = ["Informe de Salarios (Cifrado)", "Informe de Horas por Proyecto",
                    "Listado de Empleados por Departamento"]
        self.reporte_var = tk.StringVar(value=opciones[0])
        reporte_combo = ttk.Combobox(reportes_frame, textvariable=self.reporte_var, values=opciones,
                                     state='readonly', width=40)
        reporte_combo.grid(row=0, column=1, padx=10, pady=5)

        ttk.Button(reportes_frame, text="Generar PDF", style='Action.TButton').grid(row=1, column=0, padx=10,
                                                                                    pady=15, sticky='w')
        ttk.Button(reportes_frame, text="Exportar a Excel", style='Action.TButton').grid(row=1, column=1, padx=10,
                                                                                         pady=15, sticky='w')

        ttk.Label(self.content_frame,
                  text="Recuerda: Los informes de datos sensibles (como salarios) deben usar cifrado seguro para cumplir con el requisito de 'Seguridad de Datos Sensibles'.",
                  foreground='red', wraplength=700).pack(pady=10, anchor='w')

    def crear_panel_generico(self, titulo_listado: str, columnas: list, datos_ejemplo: list, entidad: str):
        """Función genérica para crear paneles de gestión (Deptos, Proyectos, etc.)."""

        listado_frame = ttk.LabelFrame(self.content_frame, text=titulo_listado, padding="15",
                                       style='Dashboard.TFrame')
        listado_frame.pack(fill='both', expand=True, pady=10)

        tree = ttk.Treeview(listado_frame, columns=columnas, show='headings', style='Treeview')

        # Scrollbar (mejora visual)
        scrollbar = ttk.Scrollbar(listado_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side='right', fill='y')
        tree.pack(side='left', fill='both', expand=True)

        # Definir encabezados
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor=tk.CENTER)

        # Poblar con datos simulados
        for item in datos_ejemplo:
            tree.insert('', tk.END, values=item)

        # Botones de Acción (CRUD genérico)
        botones_frame = ttk.Frame(self.content_frame, padding="5", style='Dashboard.TFrame')
        botones_frame.pack(fill='x', pady=10)

        ttk.Button(botones_frame, text=f"➕ Agregar {entidad}", style='Action.TButton').pack(side='left', padx=5)
        ttk.Button(botones_frame, text=f"✏️ Editar {entidad}", style='Action.TButton').pack(side='left', padx=5)
        ttk.Button(botones_frame, text=f"❌ Eliminar {entidad}", style='Action.TButton').pack(side='left', padx=5)

    def crear_panel_gestion_usuarios(self):
        """Crea la interfaz específica para gestionar Empleados/Usuarios."""

        listado_frame = ttk.LabelFrame(self.content_frame, text="Empleados Registrados", padding="15",
                                       style='Dashboard.TFrame')
        listado_frame.pack(fill='both', expand=True, pady=10)

        columnas = ("id", "nombre", "rol", "departamento", "email")
        self.empleados_tree = ttk.Treeview(listado_frame, columns=columnas, show='headings', style='Treeview')

        self.empleados_tree.heading("id", text="ID")
        self.empleados_tree.heading("nombre", text="Nombre Completo")
        self.empleados_tree.heading("rol", text="Rol")
        self.empleados_tree.heading("departamento", text="Departamento")
        self.empleados_tree.heading("email", text="Email")

        self.empleados_tree.column("id", width=80, anchor=tk.CENTER)
        self.empleados_tree.column("nombre", width=200, anchor=tk.W)
        self.empleados_tree.column("rol", width=120, anchor=tk.CENTER)
        self.empleados_tree.column("departamento", width=150, anchor=tk.CENTER)
        self.empleados_tree.column("email", width=250, anchor=tk.W)

        # Scrollbar y empaquetamiento final
        scrollbar = ttk.Scrollbar(listado_frame, orient="vertical", command=self.empleados_tree.yview)
        self.empleados_tree.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side='right', fill='y')
        self.empleados_tree.pack(side='left', fill='both', expand=True)

        botones_frame = ttk.Frame(self.content_frame, padding="5", style='Dashboard.TFrame')
        botones_frame.pack(fill='x', pady=10)

        ttk.Button(botones_frame, text="➕ Agregar Empleado", style='Action.TButton',
                   command=self.abrir_formulario_crear).pack(side='left', padx=5)
        ttk.Button(botones_frame, text="✏️ Editar Empleado", style='Action.TButton',
                   command=self.abrir_formulario_editar).pack(side='left', padx=5)
        ttk.Button(botones_frame, text="❌ Eliminar Empleado", style='Action.TButton',
                   command=self.eliminar_empleado).pack(side='left', padx=5)

        self.cargar_datos_empleados()

    def cargar_datos_empleados(self):
        self.empleados_tree.delete(*self.empleados_tree.get_children())

        datos_empleados = buscar_informacion_de_los_empleados()

        for item in datos_empleados:
            self.empleados_tree.insert('', tk.END, values=item)

    # Funciones CRUD (Mantienen la simulación por ahora)
    def abrir_formulario_crear(self):
        EmployeeForm(self.master, empleado_id=None, callback=self.cargar_datos_empleados)

    def abrir_formulario_editar(self):
        seleccion = self.empleados_tree.selection()
        if seleccion:
            empleado_id = self.empleados_tree.item(seleccion)['values'][0]
            EmployeeForm(self.master, empleado_id=empleado_id, callback=self.cargar_datos_empleados)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un empleado para editar.")

    def eliminar_empleado(self):
        seleccion = self.empleados_tree.selection()
        if seleccion:
            id_empleado = self.empleados_tree.item(seleccion)['values'][0]
            if messagebox.askyesno("Confirmar Eliminación",
                                   f"¿Estás seguro de que deseas eliminar al empleado ID {id_empleado}?"):
                print(f"Simulando eliminación de empleado ID: {id_empleado}...")
                self.cargar_datos_empleados()
        else:
            messagebox.showwarning("Advertencia", "Selecciona un empleado para eliminar.")