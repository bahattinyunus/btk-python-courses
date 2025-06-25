# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

benzinFiyat = 39.35
dizelFiyat = 41.71
lpgFiyat = 20.28

toplamYakitUcreti = 0
ortalamaYakitTuketimi = float(input("100 km' deki ortalama yakıt tüketimi: "))
gidilecekYol = float(input("Gidilen mesafe: "))
yakitTipi = input("Yakıt Tipi: ")

toplamTakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamTakitTuketimi
elif(yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamTakitTuketimi
elif(yakitTipi == "lpg"):
    toplamYakitUcreti = lpgFiyat * toplamTakitTuketimi
else:
    print("yanlış yakıt tipi")

if(toplamYakitUcreti != 0):
    print(toplamYakitUcreti)

# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

