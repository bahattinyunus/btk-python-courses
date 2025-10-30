
sayi = int(input("bir sayi girin "))

asal = True

if sayi < 2:
    asal = False
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break  
if asal:
    print(f"{sayi} bir asal sayidir")
else:
    print(f"{sayi} bir asal sayi değildir")



metin = input("bir metin gir ")

ters_metin = metin[::-1]

print("ters çevrilmiş metin:", ters_metin)




N = int(input("kaç terim görmek istiyorsun"))


ilk = 0
ikinci = 1

fib_listesi = []
for i in range(N):
    fib_listesi.append(ilk)
    toplam = ilk + ikinci
    ilk = ikinci
    ikinci = toplam
print("fibonacci listesi:")
print(fib_listesi)

