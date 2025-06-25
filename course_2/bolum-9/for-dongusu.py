# for => list
# while => koşullu

sayilar = [1,2,3,4,6,8,91,21]
isimler = ["Ali","Canan","Zeynep"]
adsoyad = "Sadık Turan"

# for x in sayilar:
#     print(x)
    
# for x in sayilar:
#     print("Merhaba BTK Akademi")

# for isim in isimler:
#     print(isim)   

# for i in adsoyad:
#     print(i)

my_tuple = [(1,2),(3,4),(5,6)]

# for a,b in my_tuple:
#     print(a,b)

my_dict = {"41":"Kocaeli","53":"Rize","35":"İzmir"}

# for x in my_dict:
#     print(my_dict[x])

for x in my_dict.values():
    print(x)

for x in my_dict.keys():
    print(x)

for x,y in my_dict.items():
    print(x,y)
