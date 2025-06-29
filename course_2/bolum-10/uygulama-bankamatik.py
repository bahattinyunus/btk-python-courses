hesaplar = [
    {
        "ad": "Bahattin Yunus Çetin",
        "hesapNo": "12345",
        "bakiye": 20000,
        "ekHesap": 5000,
        "username": "bahattinyunus",
        "password": "1234"
    },
    {
        "ad": "Efe Turan",
        "hesapNo": "12345",
        "bakiye": 30000,
        "ekHesap": 10000,
        "username": "efeturan",
        "password": "1234"
    }
]

def menu(hesap):
    print("\n")
    print(f"Merhaba, {hesap['ad']}")
    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")
    print("4- Çıkış")

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    elif islem == "4":
        print("Çıkış yapılıyor.")
        return
    else:
        print("Yanlış seçim")

    menu(hesap)

def paraYatirma(hesap):
    miktar = float(input("Yatırmak istediğiniz miktar: "))
    hesap["bakiye"] += miktar
    print(f"İşlem yapıldı, yeni bakiyeniz: {hesap['bakiye']}")

def bakiyeSorgula(hesap):
    print(f"Bakiye: {hesap['bakiye']}")
    print(f"Ek bakiye: {hesap['ekHesap']}")

def paraCekme(hesap):
    miktar = float(input("Çekmek istediğiniz miktar: "))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekHesapKullan = input("Ek hesap kullanılsın mı? (e/h): ")
            if ekHesapKullan.lower() == "e":
                kullanilacak = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kullanilacak
                print("Paranızı alabilirsiniz.")
            else:
                print("Üzgünüz, bakiyeniz yetersiz.")
        else:
            print("Üzgünüz, bakiyeniz yetersiz.")

def login():
    username = input("Username: ")
    password = input("Parola: ")

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            print("Giriş başarılı.")
            menu(hesap)
            return

    print("Username ya da parola yanlış.")

login()
