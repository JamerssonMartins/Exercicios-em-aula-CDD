#......Senha.......
#Recebendo variáveis
pin = "admin"
tentativas = 1
resposta = "Excesso de tentativas, login bloqueado"
#Conferindo se a senha está correta
while tentativas <= 3:
    senha = (input("Digite a senha:"))
    if senha == pin:
        resposta = "Login efetuado com sucesso"
        break
    tentativas += 1
print(resposta)