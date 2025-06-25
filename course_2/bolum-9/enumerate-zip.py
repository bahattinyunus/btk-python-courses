# markalar = ["opel","bmw","togg"]

# index = 1
# for marka in markalar:
#     print(f"{index}-{marka}")
#     index += 1

# obj1 = enumerate(markalar,1)

# print(type(obj1))
# print(list(obj1))

# for index,marka in enumerate(markalar,1):
#     print(f"{index}-{marka}")


# zip

numara = [100,200,300]
ogrenci = ["Ali","Ayşe","Canan","Mehmet"]

print(list(zip(numara,ogrenci)))

for no,isim in zip(numara,ogrenci):
    print(no,isim)
