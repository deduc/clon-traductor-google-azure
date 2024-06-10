"""
Requisitos funcionales:
    -hecho-• Se debe ofrecer al usuario un listado para seleccionar el idioma inicial.
    -hecho-• Se debe ofrecer al usuario un listado para seleccionar el idioma final.
    -hecho-• Se debe solicitar al usuario un texto para traducir del idioma inicial al final y mostrar el resultado.
    -hecho-• Se deben poder reproducir los textos como un audio, tanto el inicial como el final.
    -hecho-• Se debe poder introducir un audio en el idioma inicial y que se traduzca al idioma final.

Se valorará positivamente la visualización web similar a Google translator. Esta visualización debe ser intuitiva y componerse de:
    -hecho- Listado de idiomas iniciales
    -hecho- Listado de idiomas finales
    -hecho- Cuadros para ambos textos
    -hecho- Botones de reproducción de audio

Tras elegir la opción 1 o 2 se debe preguntar al usuario lo siguiente, respetando este orden:
    -hecho- Idioma inicial, mostrando una lista de idiomas numerados
    -hecho- Idioma final, mostrando una lista de idiomas numerados.

En ambos casos tras mostrar la traducción se debe preguntar al usuario si quiere reproducirla en audio.
"""


from flask import Flask, render_template, request, jsonify
from traductor import Traductor
from voz import Voz


# Creo el objeto Flask para levantar el servidor local.
app = Flask(__name__)

# Inicializo los objetos de traducción y síntesis de voz
traductor = Traductor()
voz = Voz()


# Url base. Renderiza index.html
@app.route("/")
def pagina_main():
    lista_obj_idiomas: list = traductor.obtener_lista_idiomas_disponibles()

    # todo: borrar
    contador = 0
    for obj in lista_obj_idiomas:
        if obj["nombre_idioma"] == "Español" or obj["nombre_idioma"] == "Inglés":
            print(obj)
            print(contador)
        
        contador += 1

    return render_template("index.html", lista_idiomas=lista_obj_idiomas)


# Endpoint /traducir. Resultado de mandar una peticion POST al servidor flask.
@app.route("/traducir", methods=["POST"])
def traducir_texto():
    if request.method == "POST":
        # Obtengo datos del body de la peticion del cliente
        idioma_input: str = request.json.get("idiomaInput")
        idioma_output: str = request.json.get("idiomaOutput")
        texto_input: str = request.json.get("textoInput")

        print(idioma_input, idioma_output, texto_input)
        
        texto_output: str = traductor.traducir_texto(idioma_input, idioma_output, texto_input)

        # Devuelvo el texto en un json
        return jsonify({"textoOutput": texto_output})


# Endpoint /texto_a_audio. Resultado de enviar una solicitud POST al servidor Flask.
@app.route("/texto_a_audio", methods=["POST"])
def texto_a_audio():
    if request.method == "POST":
        try:
            # Obtengo datos del cuerpo de la solicitud JSON
            data = request.get_json()
            idioma_input = data.get("idiomaInput")
            texto_input = data.get("textoInput")

            # Convierto el texto a audio y la clase Voz se encarga de hacerlo sonar.
            voz.texto_a_audio(idioma_input=idioma_input, texto_input=texto_input)

            return jsonify({"message": "Texto convertido a audio correctamente."})

        except Exception as e:
            return jsonify({"error": str(e)})


# Endpoint /audio_a_texto. Resultado de enviar una solicitud POST al servidor Flask.
@app.route("/audio_a_texto", methods=["POST"])
def audio_a_texto():
    if request.method == "POST":
        try:
            # Obtengo datos del cuerpo de la solicitud JSON
            data = request.get_json()
            idioma_input = data.get("idiomaInput")
            idioma_output = data.get("idiomaOutput")

            # La clase Voz se encarga de grabar el audio del micrófono del usuario.
            texto_traducido = voz.audio_a_texto(idioma_input, idioma_output)

            return jsonify({"message": "Audio convertido a texto correctamente.", "translated_text": texto_traducido})

        except Exception as e:
            return jsonify({"error": str(e)})


app.run()
