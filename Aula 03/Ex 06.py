#Ler o nome de 2 times e o número de gols marcados na partida
#Escrever o nome do vencedor
#CAso não haja vencedor, escrever a palavra EMPATE
print("Resultado do jogo")
T1 = str(input("Digite o nome do primeiro time: "))
G1 = int(input("Quantos gols o primeiro time marcou? "))
T2 = str(input("Digite o nome do segundo time: "))
G2 = int(input("Quantos gols o segundo time marcou? "))
if G1 > G2:
    print(f"O time {T1} venceu a partida com {G1} gols")
else:
    if G1 < G2:
        print(f"O time {T2} venceu a partida com {G2} gols")
    else:
        print(f"Os times empataram")