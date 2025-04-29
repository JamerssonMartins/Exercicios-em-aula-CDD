alunos = ['joao','carlos','maria','luiza','isabel']
print(alunos)
pesquisa = input("digite o aluno que você quer consultar: ")
for x in range(len(alunos)):
    if pesquisa == alunos[x]:
        print(f"Achei {pesquisa} na posição {x + 1}")
