customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]


customers.append("sadikturan")
order_totals.append(5000)

# Son eklenen siparişi sil
# customers.pop()
# order_totals.pop()

# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
    # '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır. (döngüler)

sonuc = f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0] + order_totals[4]} liradır"
sonuc = f"{customers[1]} isimli müşterinin sipariş toplamı {order_totals[1]} liradır"


customers.sort()  #alfabetik olarak sırala


order_totals.sort()
order_totals.reverse()   #azalan şekilde sırala


sonuc = min(order_totals)
sonuc = max(order_totals)


sonuc = customers.count('sadikturan')  #  'sadikturan' isimli kullanıcının kaç tane siparişi vardır?


customers.remove('ahmetyilmaz') # Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.

# Listelerdeki tüm içerikleri sil
# customers.clear()
# order_totals.clear()

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

username = input('müşteri adı: ')
toplam = input('toplam: ')

customers.append(username)
order_totals.append(toplam)

print(customers)
print(order_totals)

