from bs4 import BeautifulSoup
import requests
import re

# Get full code of the official page of node js and use BeautifulSoup to make web scraping
full_html = requests.get("https://nodejs.org/en/").text
html_parser = BeautifulSoup(full_html, "html.parser")


button_text = html_parser.find(class_="home-downloadbutton").text

# Use an regex to get only the numeber of the nodejs version and clean de the result
# Remove all letters, spaces and tabs
latest_version = re.sub("[\sa-zA-Z]", "", button_text)
