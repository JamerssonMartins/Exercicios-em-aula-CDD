N = int(input("Digite um número: "))
for x in range (0,N+1,1):
    for y in range (0,x+1,1):
        print(x, end=" ")
    print()
#Cheat de resolução:
#print(x*str(x), end=" ")