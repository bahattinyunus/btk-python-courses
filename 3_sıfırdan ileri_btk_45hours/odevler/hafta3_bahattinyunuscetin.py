
def ebob(a, b):
    en_buyuk = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            enBuyuk = i
    return enBuyuk



def palindrom(kelime):
    ters = kelime[::-1]  
    if kelime == ters:
        return True
    else:
        return False



def ortalama_ve_medyan(liste):

    ortalama = sum(liste) / len(liste)
    

    liste.sort()
    n = len(liste)
    if n % 2 == 1:
        medyan = liste[n // 2]
    else:
        medyan = (liste[n // 2 - 1] + liste[n // 2]) / 2
    
    return ortalama, medyan



print("ebob(24, 36) =", ebob(24, 36))
print("‘kayak’ palindrom mu", palindrom("kayak"))
print("‘merhaba’ palindrom mu", palindrom("merhaba"))
print("ortalama ve medyan", ortalama_ve_medyan([3, 5, 7, 2, 9]))
