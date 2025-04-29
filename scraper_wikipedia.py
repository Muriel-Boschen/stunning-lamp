import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

eventos = soup.select(".mw-parser-output > ul li")

wb = Workbook()
ws = wb.active
ws.title = "Eventos Atuais"
ws.append(["Manchete", "Data"])

from datetime import datetime
data_hoje = datetime.today().strftime('%Y-%m-%d')

for item in eventos:
    texto = item.get_text()
    ws.append([texto, data_hoje])


wb.save("eventos_atuais.xlsx")
print("Planilha criada com sucesso!")

