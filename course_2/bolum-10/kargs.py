def display_user(**kwargs):
    # print(type(kwargs))
    # print(kwargs)

    for key,value in kwargs.items():   #dictionary yi liste veri yapısına dönüştürüyor
        print(f"{key}: {value}")
    print("\n")

display_user(username="bahattinyunus")
display_user(username="bahattinyunus",email="bahattinyunuscetin@hotmail.com")
display_user(username="bahattinyunus",email="bahattinyunuscetin@hotmail.com", country = "Türkiye")   # değiken sayıda parametre alabiliyor
                 #liste   #dictionary
def myFunc(a,b,c,*args,  **kwargs):    #dictionary veri yapısı oluyor ** çift yıldız kullanınca
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value 1",key2="value 2")
#10
# 20
# 30
# (40, 50, 60)
# {'key1': 'value 1', 'key2': 'value 2'}