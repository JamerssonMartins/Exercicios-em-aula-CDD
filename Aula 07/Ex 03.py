alunos = [""]*5
notas = [""]*5
soma = 0
cont = 0
#Recebendo o nome dos alunos
for a in range(len(alunos)):
    alunos[a] = input("Digite o nome dos alunos: ")
print(alunos)
#Recebendo as notas dos alunos
for n in range(len(notas)):
    notas[n] = float(input(f"Digite a nota do aluno {n+1}: "))
print(notas)
#Somando as notas e calculando a média
for s in range(len(notas)):
    soma += notas[s]
media = soma/len(notas)
#Comparando para mostrar os alunos aprovados
for c in range(len(notas)):
    if notas[c] >= media:
        cont+=1
print(f"Encontramos {cont} alunos acima da média {media}")