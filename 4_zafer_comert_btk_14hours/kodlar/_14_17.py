import random
import sorting_algorithms 
import search_algorithms

# random liste
numbers = [random.randint(1,100) for _ in range(10)]
print("Liste:",numbers)

# sirali liste
numbers = sorting_algorithms.merge_sort(numbers)
print("Sıralı liste", numbers)

target = int(input("Hedef değeri giriniz: "))

ind = search_algorithms.binary_search(numbers, target, 0, len(numbers)-1)

if(ind!=-1):
    print(f"Arama sonuçlandı. Aranan eleman {ind} pozisyonunda.")
else:
    print("Aranan eleman bulunamadı.")