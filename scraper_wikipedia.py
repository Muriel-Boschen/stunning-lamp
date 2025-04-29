import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

eventos = soup.select(".mw-parser-output > ul li")
