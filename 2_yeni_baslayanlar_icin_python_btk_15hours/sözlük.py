gun = input("Türkçe gün adı..: ").lower()  # Kullanıcının girdiği gün ismini küçük harflerle alıyoruz
TrEn = {
    'pazartesi': 'monday',
    'salı': 'tuesday',
    'çarşamba': 'wednesday',  
    'perşembe': 'thursday',
    'cuma': 'friday',
    'cumartesi': 'saturday',
    'pazar': 'sunday'
}

print("İngilizcesi..:", end=" ")
print(TrEn.get(gun, 'Bu kelime sözlükte yok!'))
