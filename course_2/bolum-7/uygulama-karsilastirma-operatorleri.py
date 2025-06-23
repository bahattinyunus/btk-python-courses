not1 = int(input("not 1: "))
not2 = int(input("not 2: "))
not3 = int(input("not 3: "))

ortalama = (not1 + not2 + not3) / 3

print(f"öğrencinin not ortalaması: {round(ortalama,2)}, başarı durumu {ortalama >= 50}")