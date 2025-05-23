programlama_diller = ["Python","C#","Java","Javascript"]


sonuc = programlama_diller + ["Go","Delphi"]
print(sonuc)
sonuc = "Python" in programlama_diller
sonuc = "React" in programlama_diller       # koşul ifadeleri

del programlama_diller[0]

for dil in programlama_diller:
    print(dil)


