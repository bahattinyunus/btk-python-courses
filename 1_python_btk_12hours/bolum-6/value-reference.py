


a = ["elma","armut"]
b = ["elma","armut"]

a = b   # adres kopyaladınız.
a[0] = "üzüm"   #birinde yapılan değişiklik diğerinide etkiler çünkü a ve b aynı adresi tutuyor
print(a, b)

# liste koplayama
listeA = [10,20]
# listeB = listeA.copy()     # 1.yöntem
listeB = list(listeA)        # 2.yöntem

listeB[0] = 30

print(listeA,listeB)
