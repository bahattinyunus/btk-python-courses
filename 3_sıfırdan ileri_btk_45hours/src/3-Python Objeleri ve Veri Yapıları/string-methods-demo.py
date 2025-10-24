website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip()  # baştaki ve sondaki boşlukları siler
result = ' Hello World '.lstrip() # baştaki boşlukları siler
result = ' Hello World '.rstrip() # sondaki boşlukları siler

result = website.lstrip('/:pth') # baştaki /:pth karakterlerini siler

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = 'www.sadikturan.com'.strip('w.moc') # w.moc karakterlerini siler

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
result = course.upper()
result = course.title() # tüm kelimelerin ilk harfini büyük yapar

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a') 
result = website.count('www')
result = website.count('www',0,10) # 0. indexten 10. indekse kadar www karakterlerini sayar


# 6-  'website' içinde '.com' ifadesi var mı?
result = website.find('com')
result = website.find('com',0,10) # 0. indexten 10. indekse kadar com karakterlerini arar
result = course.find('Python')
result = course.rfind('Python')

result = website.index('com')
result = website.rindex('com')
# result = website.rindex('comm') # exception hata verir indexte ise -1 döner

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()
result = 'Hello'.isalpha()
result = course.isdigit() 
result = '123'.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50, '*') # 
result = 'Contents'.ljust(50, '*') 
result = 'Contents'.rjust(50, '*')

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ', '-')
result = course.replace(' ', '-',5) # 5 tane boşluk karakterini - ile değiştirir
result = course.replace(' ', '') # boşluk karakterlerini kaldırır

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ') # boşluk karakterlerini ayırarak liste yapar
# result = result[2]
result = result[5]

print(result)   
