#Dados:
usuarios = ['joao','carlos','mario','maria','josefa']
senhas = ['1234','3432','5432','3333','6666']
#Recebendo as informações do usuário
login = input("Digite o nome do usuário: ")
senha = (input("Digite a senha numérica de 4 dígitos: "))

for x in range(len(usuarios)):
    if login == usuarios[x]:
        if senha == senhas[x]:
            print("Login efetuado com sucesso")
        else:
            print("Usuário ou senha incorreta(o)")
if login != usuarios[x]:
    print("Usuário não encontrado")