#Ler 10 valores e mostrar quantos estão num intervalo entre 10 e 20
#e quantos não estão dentro desse intervalo
contD = 0
contF = 0
for x in range(1,11,1):
    number = int(input("Digita aí 10 números:"))
    if number >= 10 and number <= 20:
        contD += 1
    else:
        contF += 1
print(f"A quantidade de números entre 10 e 20 é: {contD}")
print(f"A quantidade de números que não está no intervalo é: {contF}")