from random import randint as r

def Islem():
    while True:
        sayi1 = r(1, 10)
        sayi2 = r(1, 10)
        islem = input("Yapmak istediğiniz işlemi belirtiniz:")
        if islem=="1":
                print("İlk Sayı: {}\nİkinci Sayı: {}\niki sayının toplamı: {}\n".format(sayi1,sayi2,sayi1+sayi2))
        elif islem=="2":
            print("İlk Sayı: {}\nİkinci Sayı: {}\nİki sayının farkı: {}\n".format(sayi1,sayi2,sayi1-sayi2))
        elif islem=="3":
            print("İlk Sayı: {}\nİkinci Sayı: {}\nİki sayının çarpımı: {}\n".format(sayi1,sayi2,sayi1*sayi2))
        elif islem=="4":
            print("İlk Sayı: {}\nİkinci Sayı: {}\nİki sayının bölümü: {}\n".format(sayi1,sayi2,sayi1/sayi2))
        elif islem=="q":
            print("Uygulamadan çıkılıyor..")
            break
        else:
            print("Tanımsız seçim..")
print("""Hoşgeldiniz..
Yapılabilecek işlemler:
1.Toplama İşlemi
2.Çıkarma İşlemi
3.Çarpma İşlemi
4.Bölme İşlemi
q.Çıkış
""")

Islem()
