

produtos = ["iphone", "ipad", "airpods"]

while True:
    novo_produto = input("Digite aqui o produto: ")
    novo_produto = novo_produto.lower()

    if "sair" == novo_produto: # condição de saída
        break

    if novo_produto in produtos:
        print("Produto já cadastrado")
    else:
        print(f"Produto {novo_produto} cadastrado com sucesso")
        produtos.append(novo_produto)

print(produtos)