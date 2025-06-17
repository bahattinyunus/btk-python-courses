# Dictionary Metotları

yemekTarifi = {
    "yemekAdi": "Musakka",
    "yemekTarifi": "tarif açıklaması",
    "resim": "1.jpg"
}

# access items
sonuc = yemekTarifi["yemekAdi"]
sonuc = yemekTarifi.get("yemekAdi")
sonuc = yemekTarifi.keys()
sonuc = yemekTarifi.values()
sonuc = yemekTarifi.items()

# update items
# yemekTarifi["yemekAdi"] = "Mantı"
# yemekTarifi.update({"yemekAdi":"Mantı"})
# yemekTarifi.update({"yemekAdi2":"Mantı"})

# delete items
# yemekTarifi.pop("yemekAdi")
# yemekTarifi.popitem()
yemekTarifi.clear()

# copy => referans

sonuc = yemekTarifi

print(sonuc)