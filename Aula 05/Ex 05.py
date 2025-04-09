#Receba 10 números e mostre quantos são negativos
contNeg = 0
for x in range(1,10,1):
    number = int(input("Digita aí 10 números:"))
    if number < 0:
        contNeg += 1
print(f"A quantidade de números negativos é: {contNeg}")
