# iki sayıyı toplayan algoritma
sayi1 = float(input("birinci sayiyi gir "))
sayi2 = float(input("ikinci sayıyı gir "))

toplam = sayi1 + sayi2
print("Toplam:", toplam)


# 5 kişilik grubun yaşlarını sıralayan algoritma
yaslar = []

yas1 = int(input("1. kişinin yaşını girin: "))
yas2 = int(input("2. kişinin yaşını girin: "))      
yas3 = int(input("3. kişinin yaşını girin: "))
yas4 = int(input("4. kişinin yaşını girin: "))
yas5 = int(input("5. kişinin yaşını girin: "))

yaslar = [yas1, yas2, yas3, yas4, yas5]
yaslar.sort()

print("Küçükten büyüğe sıralanmış yaşlar:", yaslar)

