import random

# Olası kelimeler listesinden bir tanesi rastgele seçilecek.
Liste = ["python", "print", "random", "while", "choice"]
kelime = random.choice(Liste)  # Rastgele bir kelime seçiliyor.

# Adam asmaca için kullanılan görseller
adam = [
    '''
    +------+
    o       |
   /|\\      |
   / \\      |
           ---
    ''',
    '''
    +------+
    o       |
   /|\\      |
   /        |
           ---
    ''',
    '''
    +------+
    o       |
   /|\\      |
            |
           ---
    ''',
    '''
    +------+
    o       |
   /|       |
            |
           ---
    ''',
    '''
    +------+
    o       |
            |
            |
           ---
    ''',
    '''
    +------+
            |
            |
            |
           ---
    '''
]

# Doğru ve yanlış harflerin tutulacağı listeler
dogruharf = []
yanlısharf = []
hak = len(adam)  # Oyuncunun toplam hakkı, adam listesi uzunluğuna eşit.

# Oyun döngüsü
while hak > 0:
    out = ""
    
    # Kelimenin doğru bilinen kısımlarını oluşturmak için
    for h in kelime:
        if h in dogruharf:
            out += h  # Doğru tahmin edilen harfleri göster.
        else:
            out += "_"  # Henüz doğru tahmin edilmeyen harfler boş bırakılır.
    
    # Eğer kelimenin tamamı doğru tahmin edildiyse döngüden çık.
    if out == kelime:
        break
    
    # Oyuncuya şu ana kadar doğru bilinen harfler gösterilir.
    print("Kelime: ", out)
    print(adam[len(adam) - hak])  # Kalan hakka göre adam asmaca görseli gösterilir.
    
    # Oyuncudan harf tahmini al
    girharf = input("Bir harf tahmin edin: ").lower()
    
    # Daha önce girilmiş harf kontrolü
    if girharf in dogruharf or girharf in yanlısharf:
        print(f"{girharf} zaten tahmin edildi!")
    # Eğer harf doğruysa
    elif girharf in kelime:
        print("Doğru harf!")
        dogruharf.append(girharf)  # Doğru harfi listeye ekle.
    # Harf yanlışsa
    else:
        print("Yanlış harf!")
        yanlısharf.append(girharf)  # Yanlış harfi listeye ekle.
        hak -= 1  # Hakkı bir azalt.
        
# Oyunun sonucu
if hak > 0:
    print("Tebrikler, kazandınız! Kelimeniz: ", kelime)
else:
    print("Maalesef kaybettiniz. Kelime: ", kelime, " idi.")
