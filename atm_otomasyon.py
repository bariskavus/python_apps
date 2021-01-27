print("""
Bu ATM'de yapılabilecek işlemler:
1.Para Yatırma
2.Para Çekme
3.Havale-Eft
4.Bakiye Görüntüleme
5.Çıkış
""")
def Atm():
    kullaniciBakiye = 500
    kullaniciSifre = "12345"
    while True:
        sifre = input("Lütfen şifrenizi giriniz: ")
        if sifre==kullaniciSifre:
            islemler = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
            if islemler=="1":
                yatirilanTutar=int(input("Lütfen yatırmak istediğiniz tutarı giriniz: "))
                kullaniciBakiye+=yatirilanTutar
                print("İşlem başarılı.. Yatırılan para miktarı: {}'TL\nGüncel bakiyeniz: {}'TL".format(yatirilanTutar,kullaniciBakiye))
            elif islemler=="2":
                cekilenTutar=int(input("Lütfen çekmek istediğiniz miktarı belirtiniz: "))
                if cekilenTutar>kullaniciBakiye:
                    print("Yetersiz bakiye..")
                else:
                    kullaniciBakiye-=cekilenTutar
                    print("İşlem başarılı..Çekilen para miktarı: {}'TL\nGüncel bakiyeniz: {}'TL".format(cekilenTutar,kullaniciBakiye))
            elif islemler=="3":
                havaleTutar=int(input("Lütfen göndermek istediğiniz tutarı giriniz"))
                if havaleTutar>kullaniciBakiye:
                    print("Yetersiz bakiye..")
                else:
                    hesapNo = input("Parayı göndereceğiniz hesap numarası: ")
                    kullaniciBakiye-=havaleTutar
                    print("İşlem başarılı..'{}' tanımlı hesaba {}'TL gönderildi.\nGüncel bakiyeniz: {}'TL".format(hesapNo,havaleTutar,kullaniciBakiye))
            elif islemler=="4":
                print("Güncel Bakiyeniz: {}'TL".format(kullaniciBakiye))
            elif islemler=="5":
                print("İyi Günler..")
                break
            else:
                print("Tanımsız bir seçim yaptınız..")
        else:
            print("Şifreniz yanlış")
Atm()
