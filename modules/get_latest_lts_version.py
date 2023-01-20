from bs4 import BeautifulSoup
import requests
import re

# Obtengo todo el código html de la página oficial de nodejs y uso BeautifulSoup para hacerle web scrap
full_html = requests.get("https://nodejs.org/en/").text
html_parser = BeautifulSoup(full_html, "html.parser")


button_text = html_parser.find(class_="home-downloadbutton").text

# Uso una expresión regular para obtener únicamente el número de la versión de nodejs y limpiar el resultado
# Elimina todas las letras, espacios y tabulaciones
latest_version = re.sub("[\sa-zA-Z]", "", button_text)
