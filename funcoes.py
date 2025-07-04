lista_precos = [1500, 1000, 800, 3000]

total_imposto = 0

def calcular_imposto(preco, aliquota1=0.2, aliquota2=0.15, aliquota3=0.1): # função com parâmetro
    if preco > 2000:
        imposto = preco * aliquota1
    elif preco > 1000:
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
    print(f"Preço: {preco}, Imposto: {imposto}")
    return imposto # return = retorna o valor da função

for preco in lista_precos: # chamando a função
    imposto = calcular_imposto(preco)
    total_imposto += imposto

print(f"Total do imposto: {total_imposto}")


def calcular_imposto2(preco, ir=0.275, csll=0.035, iss=0.05): # função com parâmetro
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss # retorna uma tupla

resposta = calcular_imposto2(1000)
print(resposta)