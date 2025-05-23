customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]

# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
customers.append("sadikturan")
order_totals.append(5000)

# 2- Son eklenen siparişi siliniz.
# customers.pop()
# order_totals.pop()

# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
    # '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır. (döngüler)

sonuc = f"{customers[0]} isimli müşterinin sipariş toplamı {order_totals[0] + order_totals[4]} liradır"
sonuc = f"{customers[1]} isimli müşterinin sipariş toplamı {order_totals[1]} liradır"

# 4- Müşterileri alfabetik olarak sıralayınız.
customers.sort()

# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()
order_totals.reverse()

# 6- En düşük sipariş hangisidir?
sonuc = min(order_totals)
sonuc = max(order_totals)

# 7- 'sadikturan' isimli kullanıcının kaç tane siparişi vardır?
sonuc = customers.count('sadikturan')

# 8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.
customers.remove('ahmetyilmaz')

# 9- Listelerdeki tüm içerikleri siliniz.
# customers.clear()
# order_totals.clear()

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

username = input('müşteri adı: ')
toplam = input('toplam: ')

customers.append(username)
order_totals.append(toplam)

print(customers)
print(order_totals)

