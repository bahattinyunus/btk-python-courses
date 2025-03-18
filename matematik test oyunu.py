import random

print("10 soruluk bir çarpım tablosu testi")
skor = 0

for a in range(10):
    i = random.randint(1, 10)
    x = random.randint(1, 10)
    soru = "{} * {} = ".format(i, x)
    
    dcvp = i * x
    cvp = int(input(soru))
    
    if cvp == dcvp:
        skor += 1

print("Doğru sayısı:", skor)

if skor > 8:
    print("Pekiyi")
elif skor > 6:
    print("İyi")
elif skor > 4:
    print("Orta")
else:
    print("Daha çok çalış")
