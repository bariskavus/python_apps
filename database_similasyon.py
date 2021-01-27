print("""Database Similasyonuna Hoşgeldiniz...
İşlemler:
1.Veri Ekleme
2.Veri Silme
3.Güncel Liste
4.Çıkış
""")
def DataBase():
    liste = list()
    while True:
        islem = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if islem=="1":
            giris = input("Lütfen aralara (',') yazarak veri girişi yapınız")
            eklenenVeriler = giris.split(',')
            for i in eklenenVeriler:
                liste.append(i)
            print("Veriler kaydediliyor...Güncel Liste: {}".format(liste))
        elif islem=="2":
            try:
                cıkarma = input("Lütfen silmek istediğiniz verileri (',') ile belirtiniz.")
                cikanVeriler = cıkarma.split(',')
                for i in cikanVeriler:
                    liste.remove(i)
                print("Veriler siliniyor...Güncel Liste: {}".format(liste))
            except:
                print("Veri listede mevcut değil")
        elif islem=="3":
            print("Güncel Liste: {}".format(liste))
        elif islem=="4":
            print("Database Similasyonundan çıkılıyor...")
            break
        else:
            print("Tanımlı olmayan bir işlem seçtiniz..")
DataBase()
