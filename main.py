cislo = int(input("Zadaj mi cislo z dvojkovej sustavy:"))
vysledok = 0
mocdva = 0
while cislo != 0:
    zvysok = cislo % 10
    vysledok = vysledok + zvysok * 2**mocdva
    mocdva = mocdva + 1
    cislo = cislo // 10
print(vysledok)