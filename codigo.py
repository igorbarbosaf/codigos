faturamento = 1200 # numero inteiro -> int
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1 # numero decimal -> float
mensagem = "O faturamento foi de " # string = texto ->str
teve_lucro = False # boolean = True or False -> bool

imposto = taxa_imposto * faturamento
print("Faturamento", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)
