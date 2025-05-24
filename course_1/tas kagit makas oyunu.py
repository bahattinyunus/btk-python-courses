import random
liste = ["Taş","Kağıt","Makas"]
pc=random.choice(liste) #bilgisayarın liste içinden seçtiği rastgele seçim
player=input('[Taş-Kağıt-Makas]').capitalize()
print("Bilgisayar",pc,"seçti")
print("sen",player,"seçtin")
if pc==player:
    print("berabere")
if pc=="Kağıt" and player=="Taş":
    print("kaybettin")    
if pc=="Taş" and player=="Makas":
    print("kaybettin")  
if pc=="Makas" and player=="Kağıt":
    print("kaybettin")  
if pc=="Kağıt" and player=="Makas":
    print("kazandın")    
if pc=="Taş" and player=="Kağıt":
    print("kazandın")  
if pc=="Makas" and player=="Taş":
    print("kazandın")      
else:
    print("geçerli bir seçim yapmadın")
