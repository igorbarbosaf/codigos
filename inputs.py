nome = input("Digite aqui seu nome: ")
email = input("Digite aqui seu e-mail: ")

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