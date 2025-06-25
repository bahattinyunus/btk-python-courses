# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.

# baslangic = int(input("başlangıç: "))
# bitis = int(input("bitiş: "))

# i = baslangic

# while(i < bitis):
#     if (i % 2 == 0):
#         print(i)
#     i += 1
    

# 2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.
    
# i = 100
# while (i > 0):
#     print(i)
#     i -= 1

# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# i = 0
# sayilar = []

# while (i < 5):
#     sayi = int(input("sayı: "))
#     sayilar.append(sayi)
#     i += 1

# sayilar.sort()

# print(sayilar)

# 4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.

username = ""

while not username:
    username = input("kullanıcı adı: ")

print("girilen username: " + username)

