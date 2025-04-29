import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

url = 'https://pt.wikipedia.org/wiki/Portal:Eventos_atuais'

resposta = requests.get(url)
sopa = BeautifulSoup(resposta.text, 'html.parser')

eventos = sopa.select(".mw-parser-output > ul li")

planilha = Workbook()
aba = planilha.active
aba.title = "Eventos Atuais"
aba.append(["Manchete", "Data"])

data_hoje = datetime.today().strftime('%Y-%m-%d')

for item in eventos:
    texto = item.get_text().strip()
    if texto:
        aba.append([texto, data_hoje])

planilha.save("eventos_atuais.xlsx")
print("Planilha criada com sucesso!")
