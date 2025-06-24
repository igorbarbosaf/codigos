faturamento = 1000
custo = 8100

lucro = faturamento - custo

if lucro >= 0:
    print("Lucro", lucro)
else:
    print("Prejuízo", lucro)

# if lucro > 0:
#     print("Lucro", lucro)
# elif lucro == 0:
#     print("Ponto de equilibrio", lucro)
# else:
#     print("Prejuizo", lucro)

# produtos = ["iphone", "ipad", "airpods"]
# novo_produto = input("Digite aqui o produto: ")
# novo_produto = novo_produto.lower()

# if novo_produto in produtos:
#     print("Produto já cadastrado")
# else:
#     print("Produto cadastrado com sucesso")
#     produtos.append(novo_produto)

# print(produtos)

# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus

vendas = 10000

if vendas > 15000:
    bonus = 500
elif vendas > 10000:
    bonus = 150
elif vendas > 5000:
    bonus = 50
else:
    bonus = 0

# print("Bonus", bonus)

if vendas > 5000:
    if vendas > 10000:
        if vendas > 15000:
            bonus = 500
        else:
            bonus = 150
    else:
        bonus = 50
else:
    bonus = 0

# print("Bonus", bonus)

# acima de 15000 -> 500 de bonus
# acima de 10000 -> 150 de bonus
# acima de 5000 -> 50 de bonus
# vendas da empresa > 50000

vendas = 11000
vendas_empresa = 40000
meta_empresa = 50000

if vendas > 15000 and vendas_empresa > meta_empresa: # and = e
    bonus = 500
elif vendas > 10000 and vendas_empresa > meta_empresa: # or = ou
    bonus = 150
elif vendas > 5000 and vendas_empresa > meta_empresa:
    bonus = 50
else:
    bonus = 0

print("Bonus", bonus)

if not vendas_empresa > meta_empresa: # not = não
    bonus = 0
else:
    if vendas > 15000:
        bonus = 500
    elif vendas > 10000:
        bonus = 150
    elif vendas > 5000:
        bonus = 50
    else:
        bonus = 0

print("Bonus", bonus)


# exercício desafios

# sistema de consulta de preço
precos = [1500, 1000, 800, 2000]
produtos = ["celular", "camera", "fone de ouvido", "monitor"]

