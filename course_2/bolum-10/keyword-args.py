def full_name(firstname: str, lastname: str, age: int) -> str:
    return f"Your name is {firstname} {lastname}"

sonuc = full_name("Sadık","Turan")
sonuc = full_name(lastname="Turan",firstname="Sadık")
sonuc = full_name(lastname="Turan",firstname="Sadık")
sonuc = full_name(firstname="Sadık",lastname="Turan")

print(sonuc)