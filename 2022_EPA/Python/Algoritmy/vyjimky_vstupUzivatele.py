from datetime import datetime

try:

    jmeno = input("Zadej jméno: ")
    vek = int( input("Zadej věk: ") )
    celkovy_vydelek = int(input("Zadej svuj zivotní výdělek: "))
    
    rok_narozeni = datetime.now().year - vek

    print(jmeno, vek, rok_narozeni)
    print("Průměrně jsi za rok vydělal", celkovy_vydelek / vek)

except ValueError as e:
    print("Omlouvám se, ale neumím převést váš věk nebo výdělek na číslo.")
except ZeroDivisionError as e:
    print("Věk nesmí být nula")
except Exception as e:
    print("Omlouváme se, nastala neočekávaná chyba, kontaktujte vývojáře na : email")
    print(e)






