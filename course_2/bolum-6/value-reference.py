# value types
# x = 10
# y = 20
# x = y
# y = 30
# print(x, y)

# reference

a = ["elma","armut"]
b = ["elma","armut"]

a = b   # adres kopyaladınız.
a[0] = "üzüm"
print(a, b)

# liste koplayama
listeA = [10,20]
# listeB = listeA.copy()     # 1.yöntem
listeB = list(listeA)        # 2.yöntem

listeB[0] = 30

print(listeA,listeB)
