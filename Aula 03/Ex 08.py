#Receba um número e diga se ele é par ou ímpar
number = int(input("Digite um número: "))
if number % 2 == 0:
    print(f"O número {number} é par")
else:
    print(f"O número {number} é ímpar")