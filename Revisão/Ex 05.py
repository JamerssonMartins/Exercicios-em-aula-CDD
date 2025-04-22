peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso/(altura*altura) #Ou peso/altura**2
if IMC < 18.6:
    print("Você está abaixo do peso ideal")
elif IMC >= 18.6 and IMC <= 24.9:
    print("Parabéns, você está no peso ideal")
elif IMC >= 25 and IMC <= 29.9:
    print("Você está levemente acima do peso")
elif IMC >= 30 and IMC <= 34.9:
    print("Obesidade grau I")
elif IMC >= 35 and IMC <= 39.9:
    print("Obesidade grau II (severa)")
elif IMC >= 40:
    print("Obesidade grau III (Mórbida)")