# Imports

# Imports para Web Scraping
import bs4
import csv 
import requests 
from bs4 import BeautifulSoup

# Arquivo para salvar o resultado do web scraping
arquivo = csv.writer(open('dados/nba.csv', 'w', encoding = "utf-8")) 
pagina = requests.get("https://www.basketball-reference.com/leagues/NBA_2020_per_game.html")
print(pagina)
# Requisição 200 indica sucesso na conexão
if pagina.status_code == 200:
    soup = BeautifulSoup(pagina.text, 'html.parser')
    # Busca pelo tag e classe na página HTML
    tabela = soup.find("div", {"class": "overthrow table_container"})

    # Extrai o cabeçalho da tabela (título de cada coluna) e gravamos no arquivo
    header = tabela.find("thead")
    header_elements = header.find_all("th")
    header_elements = [head.text for head in header_elements[1:]]
    arquivo.writerow(header_elements)
    # Extrai elementos de cada linha da tabela
    elementos_linha = tabela.find_all("tr", {"class": "full_table"})

    for row in elementos_linha:
        data_elements = row.find_all("td")
        data_elements = [data.text for data in data_elements]
        arquivo.writerow(data_elements)
else:
    print('Falha na conexão!')