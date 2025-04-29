numeros = [0.0]*5
for n in range(len(numeros)):
    numeros[n] = int(input(f"Digite o {n+1}º número: "))
for x in range(len(numeros)-1,-1,-1):
    print(numeros[x], end=" ")