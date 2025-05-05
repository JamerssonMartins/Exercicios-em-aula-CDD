def imprime_nome(nome):
    print(f"Olá {nome}")

def piramide(num):
    for x in range(1,num+1,1):
        for y in range (1,x+1,1):
            print(x, end=" ")
        print()

def vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1
    print(cont)

def controle_estoque(p,q,v):
    p = input("Qual o produto? ")
    q = int(input("Qual a qtd em estoque? "))
    v = float(input("Qual o valor do produto? "))
    Valor_estoque = q*v
    print(f"O produto {p} possui um valor total de R${Valor_estoque:.2f}")

def pnzero(number):
    if number > 0:
        return "P"
    elif number < 0:
        return "N"
    else:
        return "Z"

def somando(A,B):
    soma = A + B
    print(soma)

def somando_tupla(*itens):
    for x in itens:
        soma += n
    print(soma)

def somar(*itens):
    for x in itens:
        soma = sum(itens)
    print(soma)

def textoreverso(texto):
    cont = 0
    for x in range(len(texto)-1,-1,-1):
        if texto[x]!=" ":
            cont += 1
        print(texto[x], end=" ")
    print()
    print(cont)

def listas(lista):
    novaLista = []
    for x in lista:
        if x not in novaLista:
            novaLista.append(x)
    print(novaLista)

def listas2(lista):
    novalista=[]
    novalista=set(lista)
    print(novalista)