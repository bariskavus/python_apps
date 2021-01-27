
def AracKiralama(arac):
    araclar = ["Astra","Golf","Clio","Egea"]
    if arac==araclar[0]:
        if araclar.count(araclar[0]):
            print("Kiralama başarılı..\nKiralanan araç: {}".format(arac))
            araclar.remove(araclar[0])
        else:
            print("Araç şuan müsait değil..")
    elif arac == araclar[1]:
        if araclar.count(araclar[1]):
            print("Kiralama başarılı..\nKiralanan araç: {}".format(arac))
        else:
            print("Araç şuan müsait değil..")
    elif arac == araclar[2]:
        if araclar.count(araclar[2]):
            print("Kiralama başarılı..\nKiralanan araç: {}".format(arac))
        else:
            print("Araç şuan müsait değil..")
    elif arac == araclar[3]:
        if araclar.count(araclar[3]):
            print("Kiralama başarılı..\nKiralanan araç: {}".format(arac))
        else:
            print("Araç şuan müsait değil..")
    else:
        print("Araç Müsait değil")

kiralama = input("Lütfen kiralamak istediğniiz aracı belirtiniz: ")
AracKiralama(kiralama)

