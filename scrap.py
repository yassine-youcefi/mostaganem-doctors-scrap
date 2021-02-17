#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests
import json
import os
from bs4 import BeautifulSoup

# pip install virtualenv
# source venv/bin/activate
# pip3 install -r requirements.txt

url = 'http://www.dsp-mostaganem.dz/index.php/en/using-joomla/extensions/components/content-component/article-categories/153-liste-medecins-sepcialistes'

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')

data_json = []
data_csv = "Spécialité, Nom, Prénom, Adresse, Commune\n"

req2 = requests.get(url)
soup2 = BeautifulSoup(req2.text, 'html.parser')

print(soup2)
