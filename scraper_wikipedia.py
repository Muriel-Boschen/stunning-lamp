import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime


url = 'https://pt.wikipedia.org/wiki/Portal:Eventos_atuais'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

eventos = soup.select(".mw-parser-output > ul li")

wb = Workbook()
ws = wb.active
ws.title = "Eventos Atuais"
ws.append(["Manchete", "Data"])

data_hoje = datetime.today().strftime('%Y-%m-%d')

for item in eventos:
    texto = item.get_text().strip()
    if texto:
        ws.append([texto, data_hoje])

wb.save("eventos_atuais.xlsx")
print("Planilha criada com sucesso!")

