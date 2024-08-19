class Tables:
       def __init__(self) -> None:
                # creamos un dictionary con todas las sentencias sql declarando las tablas
              self.tables = {
                     'authors': self.create_authors_table(),
                     'quotes': self.create_quotes_table(),
                     'tags': self.create_tags_table(),
                     'quotes_tags': self.create_quotes_tags_table()
              }

       # tabla de autores
       def create_authors_table(self):
            return (
                "CREATE TABLE IF NOT EXISTS `authors` ("
                " `id` int(11) NOT NULL AUTO_INCREMENT,"
                " `name` varchar(100) NOT NULL,"
                " PRIMARY KEY (`id`), UNIQUE KEY `name` (`name`)"
                ") ENGINE=InnoDB"
            )
       # tabla de citas
       def create_quotes_table(self):
            return  (
                "CREATE TABLE IF NOT EXISTS `quotes` ("
                " `id` int(11) NOT NULL AUTO_INCREMENT,"
                " `quote_text` varchar(255) NOT NULL,"
                " `author_id` int(11) NOT NULL,"
                " PRIMARY KEY (`id`),"
                " FOREIGN KEY (`author_id`) REFERENCES `authors`(id)"
                ") ENGINE=InnoDB"
            )
       # tabla de categorias
       def create_tags_table(self):
           return  (
                  "CREATE TABLE IF NOT EXISTS `tags` ("
                  " `id` int(11) NOT NULL AUTO_INCREMENT,"
                  " `tag` varchar(60) NOT NULL,"
                  " PRIMARY KEY (`id`), UNIQUE KEY `tag` (`tag`)"
                  ") ENGINE=InnoDB"
           )
       # tabla para crear la relacion muchos a muchos entre citas y categorias
       def create_quotes_tags_table(self):
           return  (
                  "CREATE TABLE IF NOT EXISTS `quotes_tags` ("
                  " `quote_id` int(11) NOT NULL,"
                  " `tag_id` int(11) NOT NULL,"
                  " FOREIGN KEY (`quote_id`) REFERENCES quotes(`id`),"
                  " FOREIGN KEY (`tag_id`) REFERENCES tags(`id`)"
                  ") ENGINE=InnoDB"
           )
           

