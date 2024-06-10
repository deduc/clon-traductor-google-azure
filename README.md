# Clon de Traductor de Google
Iván Gómez Calvo
Curso Big Data & IA

---

### Requisitos funcionales. Enunciado del ejercicio.
- Se debe ofrecer al usuario un listado para seleccionar el idioma inicial.
- Se debe ofrecer al usuario un listado para seleccionar el idioma final.
- Se debe solicitar al usuario un texto para traducir del idioma inicial al final y mostrar el resultado.
- Se deben poder reproducir los textos como un audio, tanto el inicial como el final.
- Se debe poder introducir un audio en el idioma inicial y que se traduzca al idioma final.

Se valorará positivamente la visualización web similar a Google translator. Esta visualización debe ser intuitiva y componerse de:
- Listado de idiomas iniciales.
- Listado de idiomas finales.
- Cuadros para ambos textos.
- Botones de reproducción de audio.

Tras elegir la opción 1 o 2 se debe preguntar al usuario lo siguiente, respetando este orden:
- Idioma inicial, mostrando una lista de idiomas numerados.
- Idioma final, mostrando una lista de idiomas numerados.

---

## Funcionalidades de la aplicación. Casos de uso.
- El usuario entra en la aplicación web.
- El usuario puede seleccionar el idioma de entrada.
- El usuario puede seleccionar el idioma de salida.
- El usuario puede insertar texto en el cuadro de entrada de texto.
- El usuario puede clicar en el botón **Traducir**, ubicado en la parte inferior de la página, para traducir el texto.
- El usuario puede clicar en el botón **Grabar Audio** para grabar el audio recogido por el micrófono (Python se encarga de grabarlo).
- El usuario puede clicar en los dos botones **Reproducir Texto** para poder reproducir sonoramente ambos textos, tanto de entrada como de salida.

---

## Objetivos cumplidos
- Levantar servidor web con Python Flask.
- FrontEnd compuesto de html, css y javascript.
- Listado de idiomas iniciales.
- Listado de idiomas finales.
- Cuadros para ambos textos.
- Traducción de texto.
- Convertir audio a texto.
- Convertir texto a audio.

## Objetivos no cumplidos
- Mejores animaciones de los botones.
- Mostrar un elemento *dialog* para avisar al usuario cuando se está grabando audio.
- Obtener una lista de locutores para los distintos idiomas dispoibles.
