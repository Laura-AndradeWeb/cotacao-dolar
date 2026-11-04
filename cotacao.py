import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
resposta = requests.get(url)

print(resposta.status_code)
dados = resposta.json()
cotacao = dados["USDBRL"]
valor = float(cotacao["bid"])

print(f"Dólar hoje: R$ {valor:.2f} ({cotacao['create_date']})")  

import csv
with open("historico.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([cotacao["create_date"], valor])