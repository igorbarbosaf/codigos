for i in range(10):
    print("Se increva no canal")
    print(" Já se inscreveu?")

lista_precos = [1500, 1000, 800, 2000]
imposto: 0.1

for preco in lista_precos:
    imposto = preco * 0.1
    print(f"Preço: {preco} - Imposto: {imposto}")


# Regra do imposto
# Preço até 1000 -> imposto é de 10%
# Preço maior do que 1000 -> imposto é de 15%

for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f"Preço: {preco} - Imposto: {imposto}")

total_imposto = 0 # acumulado

for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f"Preço: {preco} - Imposto: {imposto}")
    total_imposto += imposto

print(f"Total do imposto: {total_imposto}")

# Exercício desafio

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15500, "mar": 17500, "abr": 16900, "mai": 16300, "jun": 18500}

# Saber quanto variou percentualmente cada mês de 2023 em comparação com 2022
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual = valor_23 / valor_22 -1
    print(f"Mês: {mes} - Variação: {var_percentual:.1%}")


# Simulem: se a empresa tivesse pelo menos empatado com 2022 nos meses que ela vendeu menos, qual teria sido o faturamento
faturamento_total_simulado = 0
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual = valor_23 / valor_22 -1 # variação percentual

    if var_percentual < 0:
        faturamento_total_simulado += valor_22
    else:
        faturamento_total_simulado += valor_23
    # print(f"Variação do mês {mes}: {var_percentual:.1%}")
print(f"Faturamento total simulado: {faturamento_total_simulado}")


for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual = valor_23 / valor_22 -1 # variação percentual

    if var_percentual < 0:
        vendas_23[mes] =valor_22
    # print(f"Variação do mês {mes}: {var_percentual:.1%}")
faturamento_total = sum(vendas_23.values())
print(faturamento_total_simulado)