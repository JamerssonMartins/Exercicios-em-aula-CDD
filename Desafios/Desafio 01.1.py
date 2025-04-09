# H1 = Entrada 1 // H2 = Entrada 2
# M1 = Entrada 1 // M2 = Entrada 2
# SH= Saída em horas // SM = Saida em minutos
# HT = Hora total (Soma de H1 + H2)
#----------------------------------------------
#Recebendo os valores
H1 = int(input("Qual o primeiro horário: "))
M1 = int(input("Qual o primeiro minuto : "))
H2 = int(input("Qual a segundo horário: "))
M2 = int(input("Qual o segundo minuto: "))
#-----------------------------------------------
HT = H1 + H2
if HT >= 24:
    SH = HT - 24
    SM = M1 + M2
    if SM >= 60:
        SH += 1
        SM -= 60
        if SH > 12:
            SH -= 12
    print(f"{SH}:{SM}")
else:
    SH = HT
    SM = M1 + M2
    if SM >= 60:
        SH += 1
        SM -= 60
        if SH > 12:
            SH -= 12
    print(f"{SH}:{SM}")


