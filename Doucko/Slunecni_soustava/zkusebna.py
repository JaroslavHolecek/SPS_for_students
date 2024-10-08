## Uloha 1
# Vytvorte funkci, ktera prijima 2D list a hezky jej printne -tzn kazdy radek zvlast a kazdou hodnotu oddeli
# carkou.
def vytiskni2Dlist(l2D):
    for radek in l2D:
        print(",".join(map(str,radek)))

## Uloha 2
# Vytvorte funkci, ktera vytvori 2D list. Fce prijima pocet radku, pocet sloupecku,
# Vraci 2Dlist
# Funkce vytvori na zaklade vstupnich hodnot 2D list a naplni jej hvezdickami a pote printne funkci z ulohy 1
def vytvor_2D_list(pocet_radku, pocet_sloupcu) :
    return [ ["*"]*pocet_sloupcu ] * pocet_radku
    # list1=[]
    # for i in range(a):
    #     list2=[]
    #     for j in range(b):
    #         list2.append("*")
    #     list1.append(list2)
    # return list1


# vytiskni2Dlist( vytvor_2D_list(5,50) )

## Uloha 3
# Vytvorte funkci, ktera vytvori 2D list. Fce prijima pocet radku, pocet sloupecku,
# Vraci 2Dlist
# Funkce vytvori na zaklade vstupnich hodnot 2D list a naplni kazdy sudy radek hvezdickami (* ) a kazdy
# lichy radek plusama (+)


def vytvor_2D_list_sudy(pocet_radku, pocet_sloupcu) :

    list1=[]
    for i in range(pocet_radku):
        list2=[]
        for j in range(pocet_sloupcu):
            if i%2==0:
                list2.append("*")
            else:
                list2.append("+")
        list1.append(list2)
    return list1

# vytiskni2Dlist( vytvor_2D_list_sudy(5,50) )

x = 10
jmeno = "Jarda"


print(f"{jmeno} má {x:10} jablek")