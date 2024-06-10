import requests
from requests import get, post


class Traductor:
    api_key = "34a36cdfac9942d7bc7b246a4df81020"
    
    api_url_idiomas_disponibles: str = "https://api.cognitive.microsofttranslator.com/languages?api-version=3.0"
    api_url_traductor: str = "https://api.cognitive.microsofttranslator.com/translate"
    
    region: str = "northeurope"

    def obtener_lista_idiomas_disponibles(self):
        # Lista de objetos idioma con atributos key_idioma y nombre_idioma
        lista_obj_idiomas_disponibles: list = []

        # Header necesario para la traducción de los idiomas disponibles al español
        headers = {"Accept-Language": "es"}

        # Llamada a la API para obtener la lista de idiomas disponibles
        response: requests.Response = get(self.api_url_idiomas_disponibles, headers=headers)
        
        # Formatear la respuesta a JSON
        data = response.json()
        # Obtengo el campo translation como diccionario
        dict_idiomas: dict = data["translation"]

        # Recorro el diccionario idiomas para crear una lista de objetos con los campos key_idioma y nombre_idioma
        for key_idioma in dict_idiomas:
            nombre_idioma = dict_idiomas[key_idioma]["name"]
            dict_aux = {"key_idioma":key_idioma, "nombre_idioma": nombre_idioma}

            lista_obj_idiomas_disponibles.append(dict_aux)
        
        return lista_obj_idiomas_disponibles

    def traducir_texto(self, idioma_input, idioma_output, texto_input):
        headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Ocp-Apim-Subscription-Region": self.region,
            "Content-Type": "application/json"
        }

        body = [{
            "text": texto_input
        }]

        params = {
            "api-version": "3.0",
            "from": idioma_input,
            "to": idioma_output
        }

        # Llamada HTTP al endpoint traductor de texto
        response = post(self.api_url_traductor, headers=headers, json=body, params=params)
        # Formateo la respuesta a JSON
        resultado = response.json()
        # Obtengo el texto traducido de la respuesta
        texto_output = resultado[0]["translations"][0]["text"]

        return texto_output
