# 3:45 (225)
# 14:20 (900)
# 6:05 (365)
#-------------
H1 = int(input("Qual a primeira hora: "))
M1 = int(input("Qual o primeiro minuto : "))
H2 = int(input("Qual a segunda hora: "))
M2 = int(input("Qual o segundo minuto: "))
#------------------------------------------------
SH = H1 + H2
SM = M1 + M2
if SM >= 60:
    SH += 1
    SM -= 60
    if SH > 24:
        SH = SH / 2
print(f"{SH}")
if SH > 12:
    SH -= 12
print(f"{SH}:{SM}")


