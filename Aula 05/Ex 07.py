#Usuário digita 5 valores
#Calcule a média dos valores lidos

#Recebendo os valores:
result = 0
for x in range(5):
    number = int(input("Digite aqui um número: "))
    result = result + number
media = result/5
print(f"A média dos números é: {media}")
