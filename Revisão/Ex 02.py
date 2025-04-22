repete = 1
while repete == 1:
    number = int(input("Digite um número: "))
    if number%2 == 0:
        if number > 0:
            print(f"O número {number} é par e positivo")
        else:
            print(f"O número {number} é par e negativo")
    else:

        if number > 0:
            print(f"O número {number} é ímpar e positivo")
        else:
            print(f"O número {number} é ímpar e negativo")
    repete = int(input("Você deseja verificar outro número?\n"
                       "Digite 1 para sim\n"
                       "Digite 2 para não\n"
                       "Digite: "))
