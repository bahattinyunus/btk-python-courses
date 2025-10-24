message = 'Hello There. My name is Sadık Turan'
message = message.split()


# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()

# message = message.strip() # baştaki ve sondaki boşlukları siler
# message = message.split() # boşlukları ayırarak liste yapar
# message = message.split('.') # noktaları ayırarak liste yapar
# message= '---'.join(message) # listeyi birleştirir ve --- ile birleştirir

# index = message.find('Sadık')
# isFound = message.startswith('H') 
# isFound = message.endswith('n') 

# message = message.replace('Sadık','Çınar')
# message = message.replace('ç','c')
#                  .replace('ö','o')
#                  .replace(' ','-')

message = message.center(50,'*')

print(message)