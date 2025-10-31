import search_algorithms

# giriş
numbers = [1, 10, 12, 4, 6, 23]

# hedef
target = int(input("Hedef değeri giriniz: "))

index = search_algorithms.linear_search(numbers, target)

if index!=-1:
    print(f"Hedef bulundu. Indeks: {index}!")
else:
    print("Hedef bulunamadı.")
