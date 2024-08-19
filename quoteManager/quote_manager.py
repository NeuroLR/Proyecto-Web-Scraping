from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError, RequestException

class QuoteManager:

    def __init__(self, url):
        self.url = url

    # esta función se encarga de obtener el codigo html de la url que pasamos al constructor
    def fetch_quotes(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status() # esta funcion lanzara una excepcion en caso de que el
            # codigo de respuesta sea 400 o mas
            # retornamos los elementos con la clase .quote
            return BeautifulSoup(response.text, "html.parser").select(".quote")
        # manejamos los distintos posibles errores que podrian ocurrir mientras scrapeamos
        except HTTPError as http_err:
            print(f"Ocurrio un HTTPError: {http_err}")
        except RequestException as req_err:
            print(f"Ocurrio un RequestException: {req_err}")
        except Exception as err:
            print(f"Ocurrio un error: {err}")
        
        return None
        
    # quote es el elemento html retornado por la funcion fetch_quotes
    def get_quote_data(self, quote):
        # dentro del elemento con la clase quote seleccionamos los elementos .text .author y .tag
        text = quote.select_one(".text").string 
        author = quote.select_one(".author").string
        tags_elements = quote.select(".tags .tag")
        tags = []
        for item in tags_elements:
            tags.append(item.string)
        return text, author, tags # retornamos el texto de cada uno de los elementos que necesitamos
    
    # la funcion get_all_quotes se encarga de llamar a las otras 2 funciones y retornar
    # la informacion obtenida de todas las citas de la pagina
    def get_all_quotes(self):
        quotes = self.fetch_quotes()
        data = []
        if not quotes:
            print("ocurrio un error obteniendo las citas")
            return data
        
        for quote in quotes:
            data.append(self.get_quote_data(quote))
            
        return data
