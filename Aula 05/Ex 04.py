number = int(input("DIgite um número: "))
if number > 0:
    for x in range(1, number + 1, 1):
        print(x, end=" ")
else:
    print("Digite um número maior que zero")