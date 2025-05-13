liste = ['ali', 'can', 'miray', 'zeynep']  # Rezervasyonu olanlar listesi
liste2 = ['bahar', 'talat']  # Rezervasyonu farklı bir gün olanlar listesi

while True:  # Sonsuz döngü
    isim = input('İsminiz nedir?.. (Çıkmak için "çıkış" yazın): ').lower()  # Girilen isim küçük harfe çevrilir

    if isim == 'çıkış':  # Kullanıcı çıkış yapmak isterse döngü sonlanır
        print("Programdan çıkılıyor...")
        break

    if isim in liste:  # Eğer isim rezervasyon listesinde varsa
        if isim == 'ali':
            masano = 5
        elif isim == 'can':
            masano = 7
        elif isim == 'miray':
            masano = 2
        elif isim == 'zeynep':
            masano = 10
        print(masano, "numaralı masada rezervasyonunuz var.")
    elif isim in liste2:  # Eğer isim başka bir gün için rezervasyon listesinde ise
        print("Rezervasyonunuz bu akşam değil.")
    else:  # İsim hiçbir listede yoksa
        print("Rezervasyonunuz yok.")
