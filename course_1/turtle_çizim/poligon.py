from turtle import*
N=int(input("köşe sayısını girin"))
aci=360/N
pensize(2)
for x in range(N) :
    forward(100)
    left(aci) 
    
circle(100,360,10)    # kısa yol  100 birim kenar uzunluğu olan bir 10 gen
    
done()



