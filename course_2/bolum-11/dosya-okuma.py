"""
    Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
    
    Kullanımı           : open(dosya_adi,dosya_erişme_modu)
    dosya_erişme_modu   : dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma modu      : okuma modu. belirtilen konumda dosya olmalıdır.
    seek                : cursor konumu
"""

f = open("log.txt", encoding='utf-8')

print(f.read())
print(f.read())

# >>> f = open("log.txt",encoding="utf-8") 
# >>> f.read()
# '1.satır\n2.satır'
# >>> f.read()
# ''
# >>> f.read()
# '\n3.satır'
# >>> f.seek(0) 
# 0
# >>> f.read()
# '1.satır\n2.satır\n3.satır'
# >>> f.read()
# ''
# >>> f.seek(10) 
# 10
# >>> f.read()   
# '2.satır\n3.satır'
# >>> f.seek(0)
# 0
# >>> f.readline()
# '1.satır\n'
# >>> f.readline()
# '2.satır\n'
# >>> f.readline()
# '3.satır'
# >>> f.readline()
# ''
# >>> f.seek(0)    
# 0
# >>> f.readlines() 
# ['1.satır\n', '2.satır\n', '3.satır']
# >>> f.seek(0)     
# 0
# >>> satirlar = f.readlines()
# >>> satirlar[0] 
# '1.satır\n'
# >>> satirlar[1] 
# '2.satır\n'
# >>> satirlar[0] 
# '1.satır\n'
# >>> satirlar
# ['1.satır\n', '2.satır\n', '3.satır']
# >>> f
# <_io.TextIOWrapper name='log.txt' mode='r' encoding='utf-8'>
# >>> f.closed
# False
# >>> f.close()
# >>> f.closed  
# True
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
# >>> f = open("log.txt",encoding="utf-8")
# >>> f.read()
# '1.satır\n2.satır\n3.satır'
# >>> f.close()
# >>>
