customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]


customers.append("sadikturan")
order_totals.append(5000)
    
customers.pop()
order_totals.pop()



sonuc = f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0] + order_totals[4]} liradır"
sonuc = f"{customers[1]} isimli müşterinin sipariş toplamı {order_totals[1]} liradır"


customers.sort()  


order_totals.sort()   #küçükten büyüğe sırala 
order_totals.reverse()   #ters çevir


sonuc = min(order_totals)  
sonuc = max(order_totals)


sonuc = customers.count('sadikturan')  


customers.remove('ahmetyilmaz') 


# customers.clear()
# order_totals.clear()


username = input('müşteri adı: ')
toplam = input('toplam: ')

customers.append(username)
order_totals.append(toplam)

print(customers)
print(order_totals)

