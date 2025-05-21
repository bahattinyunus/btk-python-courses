title = "Python ile Programlama Dersleri"

#  'Python' 
print(title[:6])

#  ilk 5 ve son 5 karakter
print(title[:6])
print(title[-8:])

# tersten yazdır
print(title[::-1])

#  Klavyeden girilen öğrenci bilgisine göre  cümleyi yazdır

ad = input('ad: ')
soyad = input('soyad: ')
not1 = input('1.not: ')
not2 = input('2.not: ')
ortalama = (float(not1) + float(not2)) / 2

sonuc = f"{ad} {soyad} isimli öğrencinin 1.notu {not1}, 2.notu {not2} ve not ortalaması {ortalama} olarak hesaplanmıştır"
print(sonuc)

