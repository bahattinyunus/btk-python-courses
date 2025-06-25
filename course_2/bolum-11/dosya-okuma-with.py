# file = open("log.txt", encoding="utf-8")

# print(file.read())

# file.close()

try:
    with open("log2.txt", encoding="utf-8") as file:
        for i in file:
            print(i, end="")
except FileNotFoundError as e:
    print("dosya okuma hatası")
