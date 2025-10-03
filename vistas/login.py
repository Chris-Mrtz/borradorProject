import tkinter as tk
from tkinter import ttk, messagebox
from cruds.crud_usuarios import buscar_usuario
from utils.validar_contrasena import verificar_contrasena
from cruds.crud_empleado import buscar_empleado_por_usuario
from cruds.crud_roles import buscar_rol
from admin_dashboard import AdminDashboard



class LoginWindow(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)
        self.pass_entry = None
        self.user_entry = None
        self.master = master
        self.title("Inicio de Sesión")
        self.geometry("400x250")
        self.resizable(False, False)

        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 10))
        style.configure('TEntry', font=('Helvetica', 10))

        self.crear_widgets()

    def crear_widgets(self):
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(expand=True, fill='both')

        # Título
        lbl_titulo = ttk.Label(main_frame, text="EcoTechSolutions - Login", font=("Helvetica", 16, "bold"),
                               foreground='#48BB78')
        lbl_titulo.grid(row=0, column=0, columnspan=2, pady=15)

        # Usuario
        ttk.Label(main_frame, text="Usuario:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.user_entry = ttk.Entry(main_frame, width=35)
        self.user_entry.grid(row=1, column=1, pady=5)

        # Contraseña
        ttk.Label(main_frame, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.pass_entry = ttk.Entry(main_frame, width=35, show="*")
        self.pass_entry.grid(row=2, column=1, pady=5)

        # Botón de Login
        btn_login = ttk.Button(main_frame, text="Iniciar Sesión", command=self.handle_login,
                               style='Accent.TButton')  # Estilo de botón principal
        btn_login.grid(row=3, column=0, columnspan=2, pady=20)

        # Configuraciones para centrar
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        # Añadir un tema para el botón principal
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Accent.TButton', background='#48BB78', foreground='white', font=('Helvetica', 10, 'bold'))
        style.map('Accent.TButton', background=[('active', '#38A169')])

    def  handle_login(self):
        """Maneja la lógica de inicio de sesión (actualmente simulada)."""
        username = self.user_entry.get()
        password = self.pass_entry.get()

        try:
            usuario_buscado = buscar_usuario(username)
            if usuario_buscado:
                resultado = verificar_contrasena(password, usuario_buscado[2])
                informacion_empleado = buscar_empleado_por_usuario(usuario_buscado[0])
                rol_empleado = buscar_rol(informacion_empleado[7])


                if resultado:
                    messagebox.showinfo("Login exitoso", f"Bienvenido!")

                    self.destroy()
                    self.master.mostrar_ventana_principal(rol_empleado[1], username)
                else:
                    messagebox.showerror("Error al ingresar", "Contraseña incorrecta.")
            else:
                messagebox.showerror("Error al ingresar", "Usuario no existe")

        except Exception as e:
            messagebox.showerror("Error con la conexion de base de datos")
            print(f"Error al ingresar: {e}")



class AppGestionEmpresarial(tk.Tk):
    """Contenedor principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión Empresarial - EcoTech Solutions")
        self.geometry("1200x700")

        self.withdraw()  # Oculta la ventana principal hasta que el login sea exitoso
        self.current_window = None

        # Iniciar el flujo con la ventana de Login
        self.login_window = LoginWindow(self)

    def mostrar_ventana_principal(self, rol: str, username: str):
        self.deiconify()

        if self.current_window:
            self.current_window.destroy()

        if rol == "admin":
            self.title(f"Sistema de Gestión Empresarial - Administrador ({username})")
            self.current_window = AdminDashboard(self)
        elif rol == "usuario_general":
            # Vista de Empleado (pendiente de desarrollo)
            self.current_window = ttk.Label(self,
                                            text=f"Panel de Empleado para {username}\n(Funcionalidad en desarrollo)",
                                            font=("Helvetica", 16))
            self.current_window.pack(expand=True, fill='both')
            self.title(f"Sistema de Gestión Empresarial - Empleado ({username})")

    def on_closing(self):
        self.destroy()


if __name__ == "__main__":
    app = AppGestionEmpresarial()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()