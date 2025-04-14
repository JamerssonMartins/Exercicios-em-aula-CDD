#......Senha.......
#Recebendo variáveis
senhaC = "admin"
senha = input("Digite sua senha: ")
x = 1
#Conferindo se a senha está correta
while senha != senhaC:
    if x < 3:
        senha = input("A senha está incorreta! \n"
            "Digite sua senha: ")
        x += 1
    else:
        print("Você excedeu o número de tentativas\n"
              "Senha bloqueada!")
        break
if senha == senhaC:
    print("Senha correta")