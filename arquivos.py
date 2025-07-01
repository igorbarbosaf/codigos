
# arquivo = open("vendas.txt", "r") # r = ler

# # fazer o que quiser com o arquivo

# arquivo. close() # fechar o arquivo

with open("vendas.txt", "r") as arquivo: # as arquivo é o nome da variável que vai receber o arquivo
    infos = arquivo.readlines() # readlines = ler o arquivo linha por linha é read = ler o arquivo inteiro
vendas_totais = 0
for item in infos:
    item = item.replace("\n", "") # replace = substituir, retirando o \n
    item = item.replace(" ", "") # tirando os espaços
    resultado = item.split(",") # split = separar
    valor = resultado[1]
    valor = float(valor)
    vendas_totais += valor

print(vendas_totais)