from quoteManager.quote_manager import QuoteManager
from mydb.mysql_database import MySqlDatabase

SERVER_HOST = "localhost" # reemplazar con el valor de su propio servidor
SERVER_USER = "root" # reemplazar con los valores de su propio servidor
SERVER_PASSWORD = "admin123" # reemplazar con los valores de su propio servidor

URL = "https://quotes.toscrape.com/"

quote_manager = QuoteManager(URL)
result = quote_manager.get_all_quotes()

db = MySqlDatabase(SERVER_HOST, SERVER_USER, SERVER_PASSWORD)

for item in result:
    db.save_data(item)

# Hardcodeado para obtener las citas de Einstein, pero puede reemplazarlo por cualquier otro autor
AUTHOR_NAME = "Albert Einstein" 
author_quotes = db.get_quotes_from_author(AUTHOR_NAME)
for quote in author_quotes:
    print(quote[0])
    

