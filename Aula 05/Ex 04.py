number = int(input("DIgite um número: "))
if number == 0:
    print("Digite um número diferente de zero")
else:
    for x in range(1,number+1,1):
        print(x, end=" ")