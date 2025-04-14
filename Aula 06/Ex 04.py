#Recebendo as variáveis
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor:  "))
#Garantindo que o divisor não seja zero
while n2 == 0:
    print("Zero não é um divisor")
    n2 = int(input("Digite o segundo número: "))
#Mostrando o resultado
resul = n1/n2
print(f"{resul:.0f}")
