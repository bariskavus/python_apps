from random import randint as r

def SayiTahmin():
    kullaniciHak = 5
    sayi = r(1,10)
    while kullaniciHak > 0:
        sayiTahmini = input("Lütfen 1 ile 10 arası bir tahminde bulununuz: ")
        if sayiTahmini==sayi:
            print("Tebrikler..Sayıyı bildiniz..")
            break
        else:
            kullaniciHak-=1
            print("Bilemediniz..Kalan hakkınız: {}".format(kullaniciHak))
            if kullaniciHak==0:
                print("Hakkınız bitti..")
SayiTahmin()

            #*******İkinci Yöntem*****

from random import randint as r

def SayıTahmin(sayi):
    deneme = 10

    while True:
        kullaniciTahmin = int(input("Lütfen 1 ile 10 arasında bir tahmin yapınız: "))
        if kullaniciTahmin==sayi:
            print("Tebrikler!!")
            break
        else:
            deneme-=1
            print("Bilemediniz. Kalan hakkınız: {}".format(deneme))
            if deneme==0:
                print("Hakkınız bitti!")
                break
tahminEdilecekSayi = r(1,10)
SayıTahmin(tahminEdilecekSayi)