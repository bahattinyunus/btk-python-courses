# open(dosya_adi,dosya_erişim_modu)
# dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.

with open("dosya.txt","r+", encoding="utf-8") as file:
    # file.seek(20)
    print(file.read())
    file.write("yeni satır\n")