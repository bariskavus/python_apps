print("""
Hoşgeldiniz, Lütfen seçiminizi yapınız;
1.Hamburger
2.Cheese Burger
3.Mini Burger
""")
hamburgerler = ["Hamburger","Cheese Burger","Mini Burger"]
hamburgerFiyat = [20,15,10]
siparis = ["E","H"]
menuFark =["Evet","Hayır"]
fark = 5

while True:
  siparisDurumu = input("Sipariş mi vermek istiyorsunuz => E/H?")
  if siparisDurumu==siparis[0]:

    while siparisDurumu==siparis[0]:
     siparisSecim = int(input("Lütfen bir hamburger çeşidi seciniz"))
     siparisAdet = int(input("Lütfen siparis miktarını giriniz"))
     if siparisSecim==1:
            secimAdi = hamburgerler[0]
            menuBüyütme=input("Menü büyütme ister misiniz (Evet-Hayır?")
            if menuBüyütme==menuFark[0]:
                toplamOdeme=(hamburgerFiyat[0]+fark)*siparisAdet
                print("*****Sipariş Onay****")
                adres = input("Lütfen ad-soyad ve adres bilgilerinizi giriniz")
                print("""
                              Seciminiz: {},
                              Siparis Miktarı: {},
                              Toplam Ödeme: {},
                              Adres Bilgisi: {},
                              Afiyet Olsun!!
                       """.format(secimAdi, siparisAdet, toplamOdeme, adres))
                break
            elif menuBüyütme==menuFark[1]:
                toplamOdeme=hamburgerFiyat[0]*siparisAdet
                print("*****Sipariş Onay****")
                adres = input("Lütfen ad-soyad ve adres bilgilerinizi giriniz")
                print("""
                              Seciminiz: {},
                              Siparis Miktarı: {},
                              Toplam Ödeme: {},
                              Adres Bilgisi: {},
                              Afiyet Olsun!!
                       """.format(secimAdi, siparisAdet, toplamOdeme, adres))
                break
            else:
                print("Tanımsız Seçim")
     elif siparisSecim==2:
            secimAdi = hamburgerler[1]
            menuBüyütme = input("Menü büyütme ister misiniz (Evet-Hayır?")
            if menuBüyütme == menuFark[0]:
                 toplamOdeme = (hamburgerFiyat[1] + fark) * siparisAdet
                 print("*****Sipariş Onay****")
                 adres = input("Lütfen ad-soyad ve adres bilgilerinizi giriniz")
                 print("""
                                               Seciminiz: {},
                                               Siparis Mikatır: {},
                                               Toplam Ödeme: {},
                                               Adres Bilgisi: {},
                                               Afiyet Olsun!!
                                        """.format(secimAdi, siparisAdet, toplamOdeme, adres))
                 break

            elif menuBüyütme == menuFark[1]:
                 toplamOdeme = hamburgerFiyat[1] * siparisAdet
                 print("*****Sipariş Onay****")
                 adres = input("Lütfen ad-soyad ve adres bilgilerinizi giriniz")
                 print("""
                                               Seciminiz: {},
                                               Siparis Miktarı: {},
                                               Toplam Ödeme: {},
                                               Adres Bilgisi: {},
                                               Afiyet Olsun!!
                                        """.format(secimAdi, siparisAdet, toplamOdeme, adres))
                 break
            else:
                 print("Tanımsız Seçim")
     elif siparisSecim==3:
            secimAdi = hamburgerler[2]
            menuBüyütme = input("Menü büyütme ister misiniz (Evet-Hayır?")
            if menuBüyütme == menuFark[0]:
                toplamOdeme = (hamburgerFiyat[2] + fark) * siparisAdet
                print("*****Sipariş Onay****")
                adres = input("Lütfen ad-soyad ve adres bilgilerinizi giriniz")
                print("""
                                              Seciminiz: {},
                                              Siparis Miktarı: {},
                                              Toplam Ödeme: {},
                                              Adres Bilgisi: {},
                                              Afiyet Olsun!!
                                       """.format(secimAdi, siparisAdet, toplamOdeme, adres))
                break
            elif menuBüyütme == menuFark[1]:
                toplamOdeme = hamburgerFiyat[2] * siparisAdet
                print("*****Sipariş Onay****")
                adres = input("Lütfen ad-soyad ve adres bilgilerinizi giriniz")
                print("""
                                              Seciminiz: {},
                                              Siparis Miktarı: {},
                                              Toplam Ödeme: {},
                                              Adres Bilgisi: {},
                                              Afiyet Olsun!!
                                       """.format(secimAdi, siparisAdet, toplamOdeme, adres))
                break
            else:
                print("Tanımsız Seçim")

  elif siparisDurumu==siparis[1]:
        print("Tekrar Bekleriz")
        break

  else:
      print("Geçerli bir giriş yapınız")









