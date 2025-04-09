#Usuário digita 5 valores
#Calcule a média dos valores lidos

#Recebendo os valores:
result = 0
for x in range(5):
    number = int(input("Digite aqui um número: "))
    result = (number * 5)/5
print(f"A média dos números é: {result}")
