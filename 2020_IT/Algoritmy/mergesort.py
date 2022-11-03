def merge(prvni_pole, druhe_pole):
    index_a = 0
    index_b = 0
    vysledek = []
    while True:
        a = prvni_pole[index_a]
        b = druhe_pole[index_b]
        if a < b:
            vysledek.append(a)
            index_a += 1
        else:
            vysledek.append(b)
            index_b += 1
        
        if index_a == len(prvni_pole):
            return vysledek + druhe_pole[index_b:]
        if index_b == len(druhe_pole):
            return vysledek + prvni_pole[index_a:]
        
    
def mergesort(pole:list):
    if len(pole) > 1:
        prvni=pole[:len(pole)//2] # první polovina pole
        druha=pole[len(pole)//2:] # druhá polovina pole
    
        prvniserazena=mergesort(prvni)
        druhaserazena=mergesort(druha)
        
        return merge(prvniserazena, druhaserazena)
    else:
        return pole
    
vstup = [2,8,4,1,5,3,9,6]
print(vstup)
hotovo = mergesort(vstup)
print(hotovo)