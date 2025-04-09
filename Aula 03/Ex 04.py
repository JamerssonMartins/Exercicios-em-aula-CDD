#Receba 2 números do usuário e mostre eles em ordem crescente
print("Vamos ordenar os números em ordem crescente")
N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
if N1>N2:
    print(f"A ordem é {N2},{N1}")
else:
    print(f"A ordem é {N1},{N2}")