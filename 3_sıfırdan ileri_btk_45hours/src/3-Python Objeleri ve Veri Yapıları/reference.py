# value types => string, number
x = 5
y = 25

x = y

y = 10

# print(x,y)

# reference types => list
a = ["apple","banana"]
b = ["apple","banana"]

a = b # a ve b aynı listeye işaret eder.

b[0] = "grape" # b listesindeki 0. indeksi "grape" yapar. a listesinde de değişir.

print(a, b) # a ve b aynı listeye işaret eder.


