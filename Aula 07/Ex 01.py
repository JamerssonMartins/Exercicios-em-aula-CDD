alunos = [""]*5
for x in range(len(alunos)):
    alunos[x] = input("Digite o nome dos alunos: ")
for x in range(len(alunos)):
    print(f"O aluno: {alunos[x]} está na posição {x+1} do array")
print(alunos)