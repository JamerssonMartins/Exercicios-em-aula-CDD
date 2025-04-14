resp = "s"
while resp == "s" or resp == "S":
    #Recebendo primeira nota
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Valor inválido\n"
                            "Digite a primeira nota: "))
    #Revcebendo segunda nota
    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Valor inválido\n"
                            "Digite a segunda nota: "))
    #Calculando e mostrando o resultado
    soma = nota1 + nota2
    media = soma/2
    print(f"A média do aluno é: {media:.2f}")
    resp = input("Deseja realizar um novo cálculo?\n"
                 "Digite Sim ou Não:")
