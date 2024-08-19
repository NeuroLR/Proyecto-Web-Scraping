import mysql.connector
from mydb.mysql_tables import Tables
from mydb.insertion_manager import InsertionManager
from mydb.selection_manager import SelectionManager

class MySqlDatabase:
    
    def __init__(self, host, user, password) -> None:
        # intentamos hacer la conexion con el servidor mysql
        self.try_to_connect_db(host, user, password, 3)
        cursor = self.db.cursor()
        self.tables = Tables().tables # obtenemos el dictionary con las tablas
        for table in self.tables.values():
            cursor.execute(table) # loopeamos los valores y ejecutamos el codigo sql

        self.insertion_manager = InsertionManager(self.db) 
        self.selection_manager = SelectionManager(self.db)

    def save_data(self, data):
        # hacemos uso de la clase InsertionManager para guardar la informacion
        self.insertion_manager.save_quote(data)

    def get_quotes_from_author(self, name):
        # Con la clase SelectionManager primero obtenemos el id del autor que coincida con el
        # nombre que pasamos como parametro y luego obtenemos las citas vinculadas a su id
        author_id = self.selection_manager.get_author_by_name(name)
        return self.selection_manager.get_author_quotes(author_id)

    def try_to_connect_db(self, host, user, password, callback_number):
        if callback_number == 0: 
            # este bloque de codigo se ejecuta cuando se acabaron los intentos por hacer la 
            # conexion
            print("fallo intentando conectar con la database")
            return None
        try:
            # intentamos conectar a la base de datos quotesDB
            self.db = mysql.connector.connect(
                host = host,
                user = user,
                passwd = password,
                database = "quotesDB"
            )
        except mysql.connector.Error:
            temp_db = mysql.connector.connect(
                host = host,
                user = user,
                passwd = password,
            )
            # en caso de ocurrir un error crearemos la database y volveremos a llamar esta misma 
            # funcion
            temp_db.cursor().execute("CREATE DATABASE IF NOT EXISTS quotesDB")
            temp_db.close()
            self.try_to_connect_db(host, user, password, callback_number-1)


        
        