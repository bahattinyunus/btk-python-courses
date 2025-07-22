i = 0
sayilar = []

while (i < 5):
    sayi = int(input("sayı: "))
    sayilar.append(sayi)
    i += 1

sayilar.sort()

print(sayilar)

# Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi 

username = ""

print(bool(username))   #fulse

while not username:
    username = input("kullanıcı adı: ")    #username dolana kadar fulse döner dolunca döngü kırıllır

print("girilen username: " + username)

