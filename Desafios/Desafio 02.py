#Receber um número e mostrar os números ímpares de zero até o número digitado

number = int(input("DIgite um número: "))
for x in range(1,number+1,1):
    if x%2!=0:
        print(x, end=" ")