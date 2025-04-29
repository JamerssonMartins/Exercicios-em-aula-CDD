#Dados:
usuarios = ['joao','carlos','mario','maria','josefa']
senhas = ['1234','3432','5432','3333','6666']
#Recebendo as informações do usuário
login = input("Digite o nome do usuário: ")
senha = (input("Digite a senha numérica de 4 dígitos: "))
sucess = 0

for x in range(len(usuarios)):
    if login == usuarios[x] and senhas[x] == senha:
        print("Login efetuado com sucesso")
        sucess = 1
if sucess != 1:
    print("Login não efetuado")
