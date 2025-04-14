#Variáveis
numA = int(input("Digite a quantidade de alunos: "))
notas = 0
x = 1
soma = 0
#Recebendo as notas
while x <= numA:
    notas = float(input("Digite a nota do aluno: "))
    soma += notas
    x += 1
#Calculando e mostrando a média
media = soma/numA
print(f"A média dos alunos é: {media}")