import os 

def save_product(product_name, file_name='products.txt'):
    
    products = read_products(file_name)
    # ürün boş mu?
    if not product_name.strip():
        print("Ürün adı boş olamaz!")
        return
    
    # ürün var mı kontrol et!
    if product_name in products:
        print("Bu ürün zaten kayıtlı!")
        return
    try:
        with open(file_name,"a", encoding="utf-8" ) as file:
            file.write(product_name + "\n")
    except Exception as e:
        print("Kayıt sırasında bir problem oluştu: ", e)
        
def read_products(file_name="products.txt"):
    if not os.path.exists(file_name):
        print("Dosya okunamadı.")
        return []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except Exception as e:
        print("Dosya okunamadı: ", e)
        return []
    
def show_products(products):
    for prd in sorted(products):
        print(prd)
        
def delete_product(product_name, file_name="products.txt"):
    products = read_products(file_name)
    if product_name in products:
        products.remove(product_name)
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                for prd in products:
                    file.write(prd +"\n")
                print(f"{product_name} ürünü silindi.")
        except Exception as e:
            print("Silme sırasında bir problem oluştu: ", e)
    else:
        print(f"{product_name} ürünü bulunamadı.")