import product_file_operations as pfo

while True:
    print("\n 1-Ürün ekle \n 2-Ürünleri Göster\n 3-Ürün Sil \n 4-Çıkış")
    choice = input("Seçim (1-4): ")
    if choice=="1":
        product = input("Ürün adı giriniz: ")
        pfo.save_product(product)
    elif choice=="2":
        pfo.show_products(pfo.read_products())
    elif choice=="3":
        prd = input("Silmek istediğiniz ürünü belirtiniz: ")
        pfo.delete_product(prd)
    elif choice=="4":
        print("Programdan çıkılıyor.")
        break
    else:
        print("Geçersiz giriş!")