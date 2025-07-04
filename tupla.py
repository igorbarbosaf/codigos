def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss

ir , csll, iss = calcular_imposto2(1000) # desempacotando a tupla
print(ir, csll, iss, sep="\n")

tamanho_tela = (1920, 1080)

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65 ,60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

# cada venda o vendedor ganha R$2 e 1% do valor de venda
# calcular o valor total de bonus pago e o bonus de cada vendedor

def calcular_bonus(lista_vendas):
    qtde = len(lista_vendas) # len = tamanho da lista
    bonus1 = qtde * 2
    valor_total = sum(lista_vendas) # sum = soma dos valores da lista
    bonus2 = 0.01 * valor_total # 0.01 = 1%
    bonus = bonus1 + bonus2

    return bonus # return = retorna o valor da função
bonus_total = 0 # acumulador
for vendedor in vendas:
    lista_vendas_vendedor = vendas[vendedor]
    bonus = calcular_bonus(lista_vendas_vendedor) # chamando a função calcular_bonus
    print(f"Vendedor: {vendedor}, Bonus: {bonus}")
    bonus_total += bonus
print(bonus_total)


# for vendedor, lista_vendas in vendas.items():
#     print(vendedor)
#     print(lista_vendas)
 