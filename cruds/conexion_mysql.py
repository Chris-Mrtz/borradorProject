import pymysql

class ConexionMySQL:

    def __init__(self):
        try:
            self.conexion = pymysql.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'test'
            )
            self.cursor = self.conexion.cursor()
            print('Conexion MySQL')
        except Exception as e:
            raise e