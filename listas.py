vendas = [100, 50, 130, 80, 120, 200]

print(vendas[0])

total_vendas = sum(vendas) # sum = soma todos os valores da lista
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130) # index = pega a posição do valor na lista
print(posicao)

print(vendas[2:])

produtos = ["iphone", "ipad", "airpods"]
precos = [4000, 8000, 2000]

# editar um item
print("iphone" in produtos)
precos[0] = precos[0] * 1.1 # 1.1 = 10% de aumento
print(precos)

# adicionar um item
produtos.append("macbook")
precos.append(10000)
print(produtos)
print(precos)

# remover um item
produtos.remove("macbook") # remove = remove o item da lista
precos.pop(-1) # pop = remove o ultimo item da lista
print(produtos)
print(precos)

# inserir um valor
produtos.insert(1, "airpods") # insert = insere um item na lista
print(produtos)

# contar valores
print(produtos.count("airpods")) # count = conta quantas vezes um valor aparece na lista

# odernar valores
precos.sort(reverse=True) # sort = ordena os valores da lista do menor para o maior, reverse=True = ordena do maior para o menor
print(precos)

# inverter valores
precos.reverse() # reverse = inverte os valores da lista
print(precos)

# juntar listas
produtos.extend(precos) # extend = junta duas listas
print(produtos)