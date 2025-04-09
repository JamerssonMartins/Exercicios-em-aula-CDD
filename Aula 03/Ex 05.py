#Faça um código que receba 4 notas de um aluno e informe se ele foi aprovado
#Considere que a média de aprovação é 7,0
#COnsidere que se a média estiver entre 4 e 6.9 o aluno está em recuperação
name = input("Digite seu nome: ")
print(f"{name}, vamos saber se vc foi aprovado ")
N1 = float(input("Digite a nota do primeiro trimestre: "))
N2 = float(input("Digite a nota do segundo trimestre: "))
N3 = float(input("Digite a nota do terceiro trimestre: "))
N4 = float(input("Digite a nota do quarto trimestre: "))
M = (N1+N2+N3+N4)/4
print(f"Sua média é: {M:.1f}")
if M>=7:
    print("Parabéns, você foi aprovado")
elif M>=4:
    print("Você está em recuperação, estude!")
else:
    print("Você foi reprovado, mas não desista!")