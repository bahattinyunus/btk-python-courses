import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

sql = "INSERT INTO genres(name) VALUES('Macera')"
cursor.execute(sql)
connection.commit()

# cursor.execute("select * from customers where city='Oslo'")
# result = cursor.fetchall()
# result = cursor.fetchone()
# print(result)
# for customer in result:
#     print(customer[1] + " " + customer[2])

connection.close()
print("veri tabanı bağlantısı hazır.")