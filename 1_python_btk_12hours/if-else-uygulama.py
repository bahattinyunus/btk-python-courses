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



