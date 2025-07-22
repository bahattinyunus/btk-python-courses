# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur.

with open("dosya.txt","w",encoding="utf-8") as file:
    file.write("Çınar Turan\n")
    file.write("Efe Turan\n")

with open("dosya.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i, end="")  #end fazladan boşluk olmaması için Her bir satır i değişkenine atanır.Normalde print() her bastığında satır sonuna \n (yeni satır) ekler. Ama end="" diyerek buna izin vermezsin.
