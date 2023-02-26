pocitadlo_kroku = 0

def najdi_setridene(pole, cislo):
    global pocitadlo_kroku
    index = len(pole) // 2
    if pole[index] == cislo:
        pocitadlo_kroku += 1
        return "tu je"
    else:
        if len(pole) == 1:
            return "tu neni"
        if pole[index] < cislo:
            pulka = pole[index+1:]
        else:
            pulka = pole[0:index]
        pocitadlo_kroku += 1
        return najdi_setridene(pulka, cislo)

def najdi_nesetridene(pole, cislo):
    global pocitadlo_kroku
    for i in pole:
        pocitadlo_kroku += 1
        if i == cislo:
            return "tu je"
    return "tu neni"
    
vstup = [1,3,5,6,7,8,9, 11, 15, 18, 17 ,19 , 24, 28, 30, 34]
vstup_n = [8,3,9,1,5,6,7, 11, 15, 17, 18, 14, 13, 12, 10 ,16]
najdi = 19
print(najdi, najdi_setridene(vstup, najdi))
print(pocitadlo_kroku)
pocitadlo_kroku = 0
print(najdi, najdi_nesetridene(vstup, najdi))
print(pocitadlo_kroku)
pocitadlo_kroku = 0
print("===============")
print(najdi, najdi_setridene(vstup_n, najdi))
print(pocitadlo_kroku)
pocitadlo_kroku = 0
print(najdi, najdi_nesetridene(vstup_n, najdi))
print(pocitadlo_kroku)
pocitadlo_kroku = 0