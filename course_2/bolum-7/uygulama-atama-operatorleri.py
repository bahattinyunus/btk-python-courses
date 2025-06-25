a, b, c = 4, 8, (12, 2)


toplam = a + b + (c[0] + c[1])

sonuc = (c[0] + c[1]) // b   # c' nin b' ye kalansız bölümü

sonuc = (a + b + (c[0] + c[1])) % 7


#  a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?
a, *b, c = (2,4,6,8,13)  # a ve b listedeki karşılıklarını alırlar   *'lı olan ise hepsini 
print(c ** 3)

# 6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?
a, b, *c = (2,4,6,8,13)  #c=6,8,13
print(c[0] + c[1] + c[2])
