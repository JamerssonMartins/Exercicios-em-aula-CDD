#Testando operadores matemáticos
#Usando as 4 principais operações
print("_______________________________")
print("Operadores matemáticos")
print("Informe dois números a calcular")
N1 = int(input("Digite o primeiro número: "))
while True:
    N2 = int(input("Digite o segundo número: "))
    if N2 == 0:
        print("Erro. Zero não édivisor, tente novamente")
    else:
        break
soma = N1+N2
subt = N1-N2
mult = N1*N2
div = N1/N2
print("_______________________________")
print(f"A soma dos números {N1} e {N2} é: {soma}")
print(f"A subtração dos números {N1} e {N2} é: {subt}")
print(f"A nultiplicação dos números {N1} e {N2} é: {mult}")
print(f"A divisão dos números {N1} e {N2} é: {div:.0f}")
print("_______________________________")