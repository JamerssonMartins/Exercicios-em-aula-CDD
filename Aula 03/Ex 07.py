#Algoritmo que leia o número de litros vendidos e o tipo de combustível
#Etanol ou Gasolina
#Imprima o valor a ser pago pelo cliente
#G = gasolina
#E = Etanol
#comb = Combustível
#LE Litros de etanol
#EA Etanol abastecido
#LG Litros de gasolina
#GA Gasolina abastecida

G = 5.80
E = 4.90
print("______________________________________")
print("Qual o combustível que será utilizado?")
print("Digite 1 para Etanol")
print("Digite 2 para gasolina")
print("______________________________________")
while True:
    comb = int(input("Digite aqui: "))
    if comb == 1:
        print("Você selecionou Etanol, o valor é R$ 4,90")
        LE = float(input("Quantos litros você quer abastecer?"))
        EA = LE * E
        print(f"Você abasteceu {LE:.0f}L de Etanol, o valor a ser pago é: {EA:.2f}")
        break
    elif comb == 2:
        print("Você selecionou Gasolina, o valor é R$ 5,80")
        LG = float(input("Quantos litros você quer abastecer?"))
        GA = LG * G
        print(f"Você abasteceu {LG:.0f}L de Gasolina, o valor a ser pago é: {GA:.2f}")
        break
    else:
        print("Digite uma opção válida")
