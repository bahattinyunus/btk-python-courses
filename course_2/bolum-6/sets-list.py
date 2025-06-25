meyveler = { "elma","armut","kiraz" }
meyveler2 = { "elma","armut","kiraz","kavun" }

# sonuc = meyveler[0] set lerde indexleme yok

# for x in meyveler:
#     print(x)

# sonuc = "elma" in meyveler

# meyveler.add("karpuz")
# meyveler.update(meyveler2)   birleştirme işlemi   
# meyveler.remove("vişne") # raise an error eleman siler ama eleman yoksa hata fırlatır
# meyveler.discard("armut")  eleman siler
# meyveler.pop()  indeksleme olmadığı için rastgele eleman siler 
meyveler.clear()     

sonuc = meyveler

print(sonuc)