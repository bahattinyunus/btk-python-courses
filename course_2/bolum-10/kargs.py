def display_user(**kwargs):
    # print(type(kwargs))
    # print(kwargs)

    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

display_user(username="sadikturan")
display_user(username="sadikturan",email="info@sadikturan.com")
display_user(username="sadikturan",email="info@sadikturan.com", country = "Türkiye")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value 1",key2="value 2")
