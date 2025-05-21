"""
    Uygulama : Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km / 1.609344
"""

mesafeKm = input("km: ")
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)
print(mesafeKm + " km= " + str(mesafeMil) + " mil")