import mysql.connector.errors


class InsertionManager:

    def __init__(self, db) -> None:
        self.db = db

    # esta es la funcion que llamaremos desde MySqlDatabase, maneja todas las demas funciones
    # ya que necesitamos guardar toda la informacion de la cita en cada tabla correspondiente
    def save_quote(self, quote):
        author_id = self.insert_author(quote[1])
        if author_id == None:
            print("fallo al guardar al autor")
            return False
        quote_id = self.insert_quote(quote[0], author_id)
        if quote_id == None:
            print("fallo al guardar la cita")
            return False
        for tag in quote[2]:
            tag_id = self.insert_tag(tag)
            self.insert_quotes_tags(quote_id, tag_id)

    # funcion encargada de guardar la informacion del autor
    def insert_author(self, name):
        try:
            cursor = self.db.cursor()
            # primero chequeamos si el autor ya existe
            cursor.execute("SELECT id FROM authors WHERE name = %s", (name,))
            result = cursor.fetchone()

            if result:
                return result[0] # en caso que exista retornamos su id
            else:
                # si no existe lo guardamos en la database
                cursor.execute(
                "INSERT INTO authors (name) VALUES (%s)",
                (name,)
                )
                self.db.commit()
                return cursor.lastrowid # la funcion retorna el id del registro recien guardado
        except mysql.connector.Error as error:
            print(f"Ocurrio un error guardando el autor: {error}")
            self.db.rollback()
            return None
    # funcion encargada de guardar la informacion de las citas
    # el parametro author_id es el id obtenido de la funcion insert_author
    def insert_quote(self, quote_text, author_id):
        try:
            cursor = self.db.cursor()
            # creamos y ejecutamos la query sql
            cursor.execute(
                "INSERT INTO quotes (quote_text, author_id) VALUES (%s, %s)",
                (quote_text, author_id)
            )
            self.db.commit()
            return cursor.lastrowid # retornamos el id de la cita recien guardada
        except mysql.connector.Error as error:
            print(f"Ocurrio un error guardando la cita: {error}")
            self.db.rollback()
            return None
        
    def insert_tag(self, tag):
        try:
            cursor = self.db.cursor()
            # buscamos si el tag ya existe en la db
            cursor.execute("SELECT id FROM tags WHERE tag = %s", (tag,))
            result = cursor.fetchone()

            if result:
                return result[0] # retornamos el id del tag si ya existe en nuestra db
            else:
                # si no existe lo guardamos
                cursor.execute(
                    "INSERT INTO tags (tag) VALUES (%s)",
                    (tag,)
                )
                self.db.commit()
                return cursor.lastrowid # y retornamos su id
        except mysql.connector.Error as error:
            print(f"Ocurrio un error guardando el tag: {error}")
            self.db.rollback()
            return None
    
    def insert_quotes_tags(self, quote_id, tag_id):
        try:
            cursor = self.db.cursor()
            # creamos la relacion muchos a muchos entre las citas y las categorias
            cursor.execute(
                "INSERT INTO quotes_tags (quote_id, tag_id) VALUES (%s, %s)",
                (quote_id, tag_id)
            )
            self.db.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Ocurrio un error guardando data en quotes_tags: {error}")
            self.db.rollback()
            return False