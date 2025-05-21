ad="Bahattin Yunus"
soyad="Çetin"
yas=40

msj= "my name is" + ad + " " + soyad + "I'm "+ str(yas)+ " years old."

msj = "my name {} {}. I'm {} years old.".format(ad,soyad,yas)
msj = "my name {0} {1}. I'm {2} years old.".format(ad,soyad,yas)
msj = "my name {a} {s}. I'm {y} years old.".format(a=ad,s=soyad,y=yas)

msj = f"my name {ad} {soyad}. I'm {yas} years old."

print(msj)