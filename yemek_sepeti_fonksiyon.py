
print("""Hoşgeldiniz..
Seçimleriniz:
1.Hamburger
2.Cheese Burger
3.Mini Burger
""")

def Hamburger(secim,menüBoy,adet,adres):
    hamburger = {1:"Hamburger",2:"Cheese Burger",3:"Mini Burger"}
    fiyat1,fiyat2,fiyat3 = 20,15,10
    fark = 5
    if secim=="1":
        if menüBoy=="E":
            print("********Sipariş Onay********\n Seçim: {}\n Adres: {}\n Toplam Ödeme: {}".format(hamburger[1],adres,(fiyat1+fark)*adet))
        elif menüBoy=="H":
            print("********Sipariş Onay********\n Seçim: {}\n Adres: {}\n Toplam Ödeme: {}".format(hamburger[1], adres, (fiyat1*adet)))
        else:
            print("Lütfen geçerli bir menü büyütme seceneği seçiniz...")
    if secim=="2":
        if menüBoy=="E":
            print("********Sipariş Onay********\n Seçim: {}\n Adres: {}\n Toplam Ödeme: {}".format(hamburger[2],adres,(fiyat2+fark)*adet))
        elif menüBoy=="H":
            print("********Sipariş Onay********\n Seçim: {}\n Adres: {}\n Toplam Ödeme: {}".format(hamburger[2], adres, (fiyat2*adet)))
        else:
            print("Lütfen geçerli bir menü büyütme seceneği seçiniz...")
    if secim=="3":
        if menüBoy=="E":
            print("********Sipariş Onay********\n Seçim: {}\n Adres: {}\n Toplam Ödeme: {}".format(hamburger[3],adres,(fiyat3+fark)*adet))
        elif menüBoy=="H":
            print("********Sipariş Onay********\n Seçim: {}\n Adres: {}\n Toplam Ödeme: {}".format(hamburger[3], adres, (fiyat3*adet)))
        else:
            print("Lütfen geçerli bir menü büyütme seceneği seçiniz...")
while True:
    siparis = input("Siparis vermek istiyor musunuz: ")
    if siparis =="E":
        secim = input("Lütfen bir hamburger seciniz")
        menüBoy =input("Ekstra patates ve içecek ister misiniz? (E/H)")
        adet = int(input("Lütfen siparis miktarını giriniz: "))
        adres = input("Lütfen ad-soyad ve adres bilgilerinizi giriniz: ")
        Hamburger(secim,menüBoy,adet,adres)
    elif siparis=="H":
        print("Yine Bekleriz..")
        break
    else:
        print("Tanımsız seçim...")



