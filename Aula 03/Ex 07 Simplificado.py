tipo = input("Qual foi o combustível utilizado?\n"
             "G = Gasolina\n"
             "E = Etanol\n"
             "Digite aqui: ")
qtdLitros = float(input("Quantos litros foram abastecidos? "))
if tipo == "G" or tipo == "g":
    valor = qtdLitros*5.8
    print(f"Você abasteceu {qtdLitros:.2f}L\n"
         f"O valor pago foi {valor:.2f}")
else:
    if tipo == "E" or tipo == "e":
        valor = qtdLitros*4.9
        print(f"Você abasteceu {qtdLitros:.2f}L\n"
              f"O valor pago foi {valor:.2f}")
    else:
        print("Opção de combustível inv álida")