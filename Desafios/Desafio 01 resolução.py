# H1 = Entrada 1 // H2 = Entrada 2
# M1 = Entrada 1 // M2 = Entrada 2
# somaH= Saída em horas // somaM = Saida em minutos
# HT = Hora total (Soma de H1 + H2)
#----------------------------------------------
#Recebendo os valores
H1 = int(input("Qual o primeiro horário: "))
M1 = int(input("Qual o primeiro minuto : "))
H2 = int(input("Qual a segundo horário: "))
M2 = int(input("Qual o segundo minuto: "))
#-----------------------------------------------

if H1 > 12:
    H1 -= 12
if H2 > 12:
    H2 -= 12
somaH = H1 + H2
if somaH > 24:
    somaH -= 12
elif somaH > 12:
    somaH -= 12
somaM = M1 + M2
if somaM >= 60:
    somaH += 1
    somaM -= 60
print(somaH,somaM)



