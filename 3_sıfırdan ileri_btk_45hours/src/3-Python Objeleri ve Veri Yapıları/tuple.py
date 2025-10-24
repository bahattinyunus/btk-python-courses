list = [1, 2, 3]
tuple = (1, 'iki', 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

# tuple listten farkılı olarak elemanlarına atama yaptırmaz
list = ['ali','veli']
tuple = ('damla','ayşe','ayşe')
names = ('demet','emel','ayşe') + tuple

print(names) # sonuç => ('demet','emel','ayşe','damla','ayşe','ayşe')

list[0] = 'ahmet'
# tuple[0] = 'deniz' # tuple elemanlarına atama yaptırmaz

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))



