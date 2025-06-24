email = "teste@teste.com"

faturamento = 1000
custo = 700

lucro = faturamento - custo

#print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")
#print("Faturamento: " + str(faturamento) + ", Custo: " + str(custo) + ", Lucro: " + str(lucro))

email = "TESTE@teste.com"

print(email.lower())
print(email.find("@")) # -1, se não encontrar o elemento. Se encontrar: a posição

posicao = email.find("@") # find = encontrar a posição de um elemento
servidor = email[posicao + 1:]
print(servidor)

# tamanho de um texto
tamanho = len(email) # len é uma função que retorna o tamanho de um texto
print(tamanho)

# trocar um pedaço do texto
email_trocado = email.replace("teste.com", "hotmail.com") # replace = trocar um pedaço do texto
print(email_trocado)

nome = "joao kira"
print(nome.capitalize()) # primeira letra maiuscula
print(nome.title()) # todas as palavras com a primeira letra maiuscula

# especiais - formatação numerico
margem = lucro / faturamento
print(f"Faturamento: R${faturamento:,.2f}\nCusto: {custo}\nLucro: {lucro}") # :,.2f = formatação numerica
print(f"Margem: {margem:.1%}")

# exercícios
nome = "Igor Barbosa"
email = "igor@barbosa.com"

# descubra o servidor do email
posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

# pegar o primeiro nome do usuário
posicao = nome.find(" ")
primeiro_nome = nome[:posicao] # [:] = pegar um pedaço do texto
print(primeiro_nome)

# contrua uma mensagem: Usuário primeiro_nome cadastrado com sucesso com o email tal
mensagem = f"Usuário {primeiro_nome} cadastrado com sucesso com o email {email}"
print(mensagem)

# contrua uma mensagem: Enviamos um link de confirmação para o email i***@gmail.com
primeira_letra = email[0]
print(primeira_letra)
mensagem = f"Enviamos um link de confirmação para o email {primeira_letra}***{servidor}"
print(mensagem)
