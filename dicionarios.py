precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

dic_precos = {"celular": 1500,
              "camera": 1000,
              "fone de ouvido": 800,
              "monitor": 2000}

# pegar um item
preco_celular = dic_precos["celular"]
print(preco_celular)

dic_precos["celular"] = 2000
print(dic_precos)

dic_precos["iphone"] = 4500
print(dic_precos)

dic_precos.pop("iphone")
print(dic_precos)

# tamanho do dicionário
print(len(dic_precos)) # len = contar quantos itens tem no dicionário

print(dic_precos.keys()) # keys = pegar as chaves do dicionário
print(dic_precos.values()) # values = pegar os valores do dicionário
print(dic_precos.items()) # items = pegar as chaves e valores do dicionário

# exercício
dic_precos = {"celular": 1500,
              "camera": 1000,
              "fone de ouvido": 800,
              "monitor": 2000}

produto_procurado = input("Digite o produto que você deseja consultar: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in dic_precos:
    preco = dic_precos[produto_procurado]
    print(f"Produto: {produto_procurado} - Preço: {preco}")
else:
    print("Produto não encontrado, tente novamente!")