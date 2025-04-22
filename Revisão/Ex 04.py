SalMin = float(input("Digite o salário mínimo: ")) #Salário mínimo
SalAtual = float(input("Digite seu salário atual: ")) #Salário atual
while SalAtual != 0:
    result = SalAtual / SalMin
    print(f"Você recebe {result:.1f}x do salário mínimo")
    SalAtual = float(input("Digite seu salário atual: "))
print("Programa encerrado")