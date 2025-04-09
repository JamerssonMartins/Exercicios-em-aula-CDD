#Informando o nome, idade e salário do usuário:
#Em seguida informando o percentual de aumento e salário pós aumento
name = input("Qual o seu nome? ")
age = int(input("Qual sua idade? "))
salario = float(input("Qual seu salário? "))
aumento = float(input("Qual a porcentagem do aumento salarial? "))
percentual = (aumento/100)*salario
novosalario = (aumento/100)*salario+salario
print(f"Olá {name}, sua idade é {age} anos e você recebe R${salario:.2f}")
print(f"Congratulations! Você recebeu um aumento de {aumento:.2f}%, sendo: R${percentual:.2f}")
print(f"Após o aumento seu salário passou a ser: R${novosalario:.2f}")