#importação de bibliotecas
import requests #biblioteca que faz pedidos na internet
from datetime import datetime #traz a ferramenta datetime da biblioteca datetime
import csv #biblioteca que sabe ler e escrever arquivos csv

#pega os dados da API
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL" #variável recebe o endereço da API
resposta = requests.get(url) #guarda a informação da API em resposta

#ver se deu certo (200 = deu certo; 404 = não encontrei; 500 = erro no servidor deles)
print(resposta.status_code)

dados = resposta.json() #transfroma o texto que veio da API em um dicionário Python
cotacao = dados["USDBRL"] #abre a primeira caixa USDBRL que esta em dados
valor = float(cotacao["bid"]) #pega o valor do dólar que esta em bid e tranforma em float

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