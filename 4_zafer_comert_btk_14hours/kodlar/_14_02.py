# Kütüphane dahil etme
import operations

# Giriş
n = int(input("Faktöriyeli hesaplanacak sayıyı giriniz: "))

# Hesaplama yap
result = operations.recursive_factorial(n)

# Çıktı
print(f"{n}! = {result}")
