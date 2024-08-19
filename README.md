# Proyecto: Web Scraping y Almacenamiento en Base de Datos

## Explicación del codigo
El codigo se divide en 3 partes: main.py, quoteManager y mydb
main.py es donde ejecutaremos el codigo, tambien donde pondremos los datos de nuestro servidor
localhost para poder ejecutar el codigo MySQL.

quoteManager es la sección con el codigo que se encarga del web scraping.
La clase QuoteManager obtendrá las citas de la pagina web proporcionada, filtrara el codigo
HTML para obtener el texto, autor y categorias de la cita.
Luego retornara un array con toda la información de las citas obtenidas.

Finalmente la parte de mydb, consta de 4 archivos mysql_database.py el cual se conectará
con el servidor de MySQL y usará las otras 3 clases para manejar la información.
mysql_tables.py se encarga de crear las tablas que usaremos en nuestra database.
insertion_manager.py contiene la clase InsertionManager la cual se encarga de toda la logica
respecto a la inserción de los datos.
Por ultimo selection_manager.py que contiene la clase SelectionManager la cual se encarga de
leer la información guardada en nuestra base de datos.

## Uso
Antes de iniciar el proyecto reemplazar los valores de las variables SERVER_HOST, SERVER_USER y
SERVER_PASSWORD con los valores de su servidor MySQL, no es necesario que tenga una base de datos ya creada, la clase MySqlDatabase del archivo mysql_database.py se encargara de crear una base de datos con el nombre quotesdb.

Recuerda instalar las dependencias del proyecto haciendo uso del requirements.txt

Una vez esta todo listo puede ejecutar el codigo usando con el comando "python main.py" o
"python3 main.py"