1| import requests
2| from bs4 import BeautifulSoup
3| from openpyxl import Workbook
4| from datetime import datetime
5| import sys
6| import os
7| sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
8| 
9| 
10| url = 'https://pt.wikipedia.org/wiki/Portal:Eventos_atuais'
11| 
12| response = requests.get(url)
13| soup = BeautifulSoup(response.text, 'html.parser')
14| 
15| eventos = soup.select(".mw-parser-output > ul li")
16| 
17| wb = Workbook()
18| ws = wb.active
19| ws.title = "Eventos Atuais"
20| ws.append(["Manchete", "Data"])
21| 
22| data_hoje = datetime.today().strftime('%Y-%m-%d')
23| 
24| for item in eventos:
25|     texto = item.get_text().strip()
26|     if texto:
27|         ws.append([texto, data_hoje])
28| 
29| wb.save("eventos_atuais.xlsx")
30| print("Planilha criada com sucesso!")
