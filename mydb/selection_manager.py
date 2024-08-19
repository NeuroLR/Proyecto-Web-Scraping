import mysql.connector.errors

class SelectionManager:

    def __init__(self, db) -> None:
        self.db = db

    # funcion para obtener el id del autor buscando por nombre
    def get_author_by_name(self, name):
        try:
            cursor = self.db.cursor()
            # creamos y ejecutamos la query 
            cursor.execute("SELECT id FROM authors WHERE name = %s", (name,))
            result = cursor.fetchone() # la funcion fetchone nos retornara un unico valor
            return result[0] or -1
        except mysql.connector.Error as error:
            print(f"Ocurrio un error en getAuthorByName: {error}")
            return -1
    
    # funcion para obtener todas las citas creadas por un autor en concreto
    def get_author_quotes(self, author_id):
        try:
            cursor = self.db.cursor()
            # creamos y ejecutamos la query utilizando el id del autor que obtuvimos usando
            # la funcion anterior
            cursor.execute("SELECT quote_text FROM quotes WHERE author_id = %s", (author_id,))
            result = cursor.fetchall() # en este caso utilizamos fetchall ya que queremos 
            # obtener todas las citas que existan
            return result
        except mysql.connector.Error as error:
            print(f"Ocurrio un error en getAuthorQuotes: {error}")
            return None