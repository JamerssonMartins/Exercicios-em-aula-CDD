N = int(input("Digite um número: "))
for x in range (1,N+1,1):
    for y in range (1,x+1,1):
        print(x, end="")
#Cheat de resolução:
#print(x*str(x), end=" ")