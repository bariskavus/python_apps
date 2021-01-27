def UrunReyon():
    while True:
        urunAdi = input("Aradığınız ürün adını giriniz: ")
        if urunAdi=="Domates" or urunAdi=="Biber" or urunAdi=="Brokoli":
            print("Lütfen sebze reyonuna gidiniz..")
        elif urunAdi=="Diş macunu" or urunAdi=="Parfüm" or urunAdi=="Şampuan":
            print("Lütfen kozmetik reyonuna gidiniz..")
        elif urunAdi=="Cep telefonu" or urunAdi=="Bilgisayar":
            print("Lütfen teknoloji reyonuna gidiniz..")
        else:
            print("Aradığınız ürün şuan mevcut değildir..")
UrunReyon()
