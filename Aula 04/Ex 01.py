print("Escolhe um mês:")
meses = ["1 - Janeiro", "2 - Fevereiro", "3 - Março", "4 - Abril", "5 - Maio", "6 - Junho",
         "7 - Julho", "8 - Agosto", "9 - Setembto", "10 - Outubro", "11 - Novembro", "12 - Dezembro"]
for mes in meses:
    print(mes)
number = int(input("Digite um número de 1 a 12: "))
if number == 1:
    print("Janeiro")
elif number == 2:
    print("Fevereiro")
elif number == 3:
    print("Março")
elif number == 4:
    print("Abril")
elif number == 5:
    print("Maio")
elif number == 6:
    print("Junho")
elif number == 7:
    print("Julho")
elif number == 8:
    print("Agosto")
elif number == 9:
    print("Setembro")
elif number == 10:
    print("Outubro")
elif number == 11:
    print("Novembro")
elif number == 12:
    print("Dezembro")
else:
    print("Opção inválida, digite um número de 1 a 12")

