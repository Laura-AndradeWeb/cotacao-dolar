#importação de bibliotecas
import requests #biblioteca que faz pedidos na internet
from datetime import datetime #traz a ferramenta datetime da biblioteca datetime
import csv #biblioteca que sabe ler e escrever arquivos csv
import sys #biblioteca que permite encerrar o programa

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL" #variável recebe o endereço da API

try:
    resposta = requests.get(url, timeout=10) #guarda a informação da API em resposta; se a APi não responder em 10seg. o programa desiste
    resposta.raise_for_status() #se a resposta for um erro ele gera um erro
    dados = resposta.json() #transfroma o texto que veio da API em um dicionário Python
    cotacao = dados["USDBRL"] #abre a primeira caixa USDBRL que esta em dados
    valor = float(cotacao["bid"]) #pega o valor do dólar que esta em bid e tranforma em float

#pega o problema e imprime
except requests.exceptions.RequestException as erro:
    print(f"Não consegui buscar a cotação: {erro}")
    sys.exit(1)

#caso a API responder mas com um formato diferente do esperado
#keyError: caso USDBRL ou bid não existirem
#ValueError: caso float() não conseguir converter
except (KeyError, ValueError):
    print("A API respondeu em um formato inesperado.")
    sys.exit(1) #encerra o programa; 1 indica que terminou com erro

#mostra o valor e o horário/data da cotação 
print(f"Dólar hoje: R$ {valor:.2f} ({cotacao['create_date']})") 

#guarda a hora e a data do computador nesse instante; e define o formato que serão armazenadas
agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#salvar no CSV
#respectivamente: abre o arquivo(se não existir cria);
#                 "a" = append (acrecenta no final sem apagar o que já está escrito);
#                 evita linhas em branco no Windows;
#                 acentuação
with open("historico.csv", "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo) #cria o escritor CSV
    escritor.writerow([agora, cotacao["create_date"], valor]) #define o que terá em cada linha