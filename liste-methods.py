sayilar = [4,6,8,2,56,78,90,4,4]
isimler = ['ahmet','canan','zeynep','gökhan','ali','canan']

sonuc = min(sayilar)
sonuc = min(isimler)
sonuc = max(isimler)
sonuc = max(sayilar)

 
sayilar.append(12)
isimler.append('çınar')

sayilar.insert(0, 100) #hep sağa ekler 0. indisi sağa kaydırır onun yerine geçer 
sayilar.insert(-1, 100) # sınuncu indisi sağa kaydırır ve onun yerine geçer
sayilar.insert(len(sayilar), 100)


sayilar.pop() #sondaki elemanı siler
sayilar.pop(0)
isimler.remove('canan')


sayilar.sort()  #düz sıralar
isimler.sort()
sayilar.reverse()  #ters sıralar

 
sonuc = sayilar.index(4)  # 4. index te ne var

sonuc = sayilar.count(4) #listedeki 4 leri sayar
sonuc = isimler.count('canan')

print(sonuc)