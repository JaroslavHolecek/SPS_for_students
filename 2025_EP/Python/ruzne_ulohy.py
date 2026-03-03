import re # regular expresion

# 1) Dlouhý text a) Spočítat všechny znaky b) spočítat znaky bez mezer c) spočítat slova
def pocty_v_textu(vstupni_text):
    vsechny_znaky = len(vstupni_text)

    bez_mezer = len( vstupni_text.replace(" ", "") )

    pocet_slov = len( re.sub("\W", " ", vstupni_text).split(" ") )

    return vsechny_znaky, bez_mezer, pocet_slov

# 2) "Rejstřík" - seznam unikátních slov (seřazené podle abecedy)
def rejstrik(vstupni_text):
    
    unikatni = set( re.sub("\W", " ", vstupni_text).split(" ") )
    serazene = sorted(unikatni)

    return serazene

# 3) Počet, kolikrát se v textu objevuje každé slovo

# 4) Program, který vypisuje (donekonečna) řadu čísel:
#   a) od 1 do 9: 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 ...
#   b) od 1 do 9 a zpet: 1 2 3 5 4 6 7 8 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 ...
#   c) licha a pak suda: 1 3 5 7 9 2 4 6 8 1 3 5 7 9 2 4 ...
#   d) jednu 1 dve 2 tri 3 atd... 1 22 333 4444 55555 666666 7777777 88888888 ...
    
text = "Překladač (též kompilátor, anglicky translator nebo také compiler z to compile – sestavit, zpracovat) je v nejčastějším smyslu slova softwarový nástroj používaný programátory pro vývoj softwaru. Kompilátor slouží pro překlad algoritmů zapsaných ve vyšším programovacím jazyce do jazyka nižšího, nejčastěji strojového, či spíše do strojového kódu. Z širšího obecného hlediska je kompilátor stroj, respektive program, provádějící překlad z nějakého vstupního jazyka do jazyka výstupního. Z matematického hlediska je kompilátor funkce, která mapuje jeden nebo více zdrojových kódů podle překladových parametrů na kód ve výstupním jazyce."




vysledek = rejstrik(text)
print(vysledek)


