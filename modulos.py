import os # os permite criar, ler, escrever, deletar, etc.

lista_arquivos = os.listdir("arquivos") #listdir = lista todos os arquivos do diretório atual
print(lista_arquivos)

for nome_arquivo in lista_arquivos:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")

import requests # requests permite fazer requisições HTTP

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
dic_resposta = resposta.json()
print(dic_resposta)
cotacao_dolar = dic_resposta["USDBRL"] # USDBRL é o código da moeda que queremos pegar a cotação
print(cotacao_dolar ["bid"]) # bid é o campo que contém a cotação do dólar em tempo real