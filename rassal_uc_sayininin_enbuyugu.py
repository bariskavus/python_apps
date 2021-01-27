from random import randint as r

def EnBuyuk(birinciSayi,ikinciSayi,ucuncuSayi):
    if birinciSayi > ikinciSayi > ucuncuSayi:
        print("Rassal değerler => {},{},{}, En büyük değer => {}".format(birinciSayi, ikinciSayi, ucuncuSayi,birinciSayi))
    elif birinciSayi > ucuncuSayi > ikinciSayi:
        print("Rassal değerler => {},{},{}, En büyük değer => {}".format(birinciSayi, ikinciSayi, ucuncuSayi, birinciSayi))
    elif ikinciSayi > birinciSayi > ucuncuSayi:
        print("Rassal değerler => {},{},{}, En büyük değer => {}".format(birinciSayi, ikinciSayi, ucuncuSayi, ikinciSayi))
    elif ikinciSayi > ucuncuSayi > birinciSayi:
        print("Rassal değerler => {},{},{}, En büyük değer => {}".format(birinciSayi, ikinciSayi, ucuncuSayi, ucuncuSayi))
    elif ucuncuSayi > ikinciSayi > birinciSayi:
        print("Rassal değerler => {},{},{}, En büyük değer => {}".format(birinciSayi, ikinciSayi, ucuncuSayi, ucuncuSayi))
    elif ucuncuSayi > birinciSayi > ikinciSayi:
        print("Rassal değerler => {},{},{}, En büyük değer => {}".format(birinciSayi, ikinciSayi, ucuncuSayi, ucuncuSayi))
    else:
        print("Rassal değerler => {},{},{}, Sayılar birbirine eşittir".format(birinciSayi, ikinciSayi, ucuncuSayi))
sayi1 = r(1,50)
sayi2 = r(1,50)
sayi3 = r(1,50)
EnBuyuk(sayi1,sayi2,sayi3)