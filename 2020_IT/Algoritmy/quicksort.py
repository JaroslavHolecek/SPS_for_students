sort = [5,3,61,65,33,8,4,7,5,9,4,6,1,2,3]
def quick(pole):
    if len(pole) <=1:
        return pole
    pivot=pole[0]
    mensi=[]
    vetsi=[]
    for p in pole[1:]: # [1:] znamená projdi pole až od 2. čísla dál
        if pivot > p:
            mensi.append(p)
        else:
            vetsi.append(p)
    return quick(mensi)+[pivot]+quick(vetsi)
    
            

print(sort)
serazene = quick(sort)
print(serazene)
