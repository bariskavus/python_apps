def Fibonacci(sayi):

    birinciSayi = 0
    ikinciSayi = 1

    if sayi < 0:
        print("Girdiğinz sayi ({}), negatif bir sayıdır.!!".format(sayi))

    else:

     for x in range(sayi):
            deger = ""
            deger += str(birinciSayi)
            print(deger)
            toplam = birinciSayi+ikinciSayi
            birinciSayi=ikinciSayi
            ikinciSayi=toplam
taban = int(input("Lütfen bir sayı giriniz: "))
Fibonacci(taban)