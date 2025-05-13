# -*- coding: utf-8 -*-
l = []  # Hasta listesini tutmak için bir liste
while True:
    TC = input("TC gir..: ")
    if TC in l:  # Eğer TC listede varsa
        i = l.index(TC)
        print("Muayene sırası..:", i + 1)
    elif TC == "0":  # Eğer giriş '0' ise
        if l:  # Liste boş değilse
            print(l[0], 'TC numaralı hasta doktorun yanına gidiniz.')
            l.pop(0)  # İlk sıradaki hastayı listeden çıkar
        else:
            print("Bekleyen hasta yok.")
    else:  # Yeni bir TC numarası girildiğinde
        l.append(TC)
        print(TC, 'TC numaralı hasta sıraya alındı.')
