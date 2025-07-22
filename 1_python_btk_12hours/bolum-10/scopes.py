# local scope
# global scope

# x = "global scope"

# def my_func():
#     x = "local scope"
#     print(x)

# my_func()
# print(x)

# name = "Çınar"

# def change_name(new_name):
#     global name
#     name = new_name
#     print(name)

# change_name("Ada")
# print(name)
# name = "global string"

# def greeting():
#     # name = "Çınar"

#     def hello():
#         # name = "Ada"
#         print("hello ", name)

#     hello()

# greeting()


x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)