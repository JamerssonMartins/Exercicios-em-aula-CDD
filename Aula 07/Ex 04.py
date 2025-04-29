numeros = [""]*5
M = 0
#REcebendo os números
for a in range(len(numeros)):
    numeros[a] = int(input(f"Digite o {a+1}º número: "))
#Multiplicação dos números pela var X
X = int(input("Digite o número multiplicador: "))
for x in range(len(numeros)):
    M = numeros[x]*X
    print(M, end=" ")
