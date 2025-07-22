mesaj = "btk akademi, python kursu"


sonuc1 = mesaj.title()  #tüm kelimelerin ilk harfi
sonuc2 = mesaj.capitalize() #sadece ilk harf

sonuc3 = "abc".islower() 
sonuc4 = mesaj.strip() #baştaki sondaki karakteri siler
sonuc5 = mesaj.split() #boşluğa bakarak kelimeleri anlar ve bir dizinin elemanları olarak listeler
sonuc6 = mesaj.split(',') #virgüle göre 

sonuc7 = mesaj.index("akademi") #akademi kelimesi hangi index ten başlıyor  
sonuc8 = mesaj.startswith("a") #a ile mi başlıyor
sonuc9 = mesaj.endswith("u") 

sonuc = mesaj.replace("python","javascript")  #  ** pythonu javascriptle değiştir
print("1---"+sonuc1)
print("2---"+sonuc2)
print("3---"+str(sonuc3))
print("4---"+sonuc4)
print("5---"+str(sonuc5))
print("6---"+str(sonuc6))
print("7---"+str(sonuc7))
print("8---"+str(sonuc8))
print("9---"+str(sonuc9))
print("10---"+sonuc)