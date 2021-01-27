
#iki kullanıcı rastgele sayılarla (1,6 aralığında) zar atıyor.
#Oyun bir oyuncu kaybedene kadar devam etsin.
#Zarlar eşit gelirse bahisler iade edilsi.

from random import randint as r

kullaniciBakiye1,kullaniciBakiye2=500,500
havuz=0
while kullaniciBakiye1>0 and kullaniciBakiye2>0:
    while True:
        kullanici1Bahis = int(input("Birinci oyuncu; Lütfen bahsinizi giriniz."))
        if kullanici1Bahis>kullaniciBakiye1:
            print("Birinci oyunucunun bahisi bakiyesini aşmaktadır.")
            continue # Burada continue dediğimiz zaman bu if mekanizması çalışştığı zaman kişiyi tekrar while döngüsünün başına döndürüyoruz.
        kullanici2Bahis = int(input("İkinci oyuncu; Lütfen bahsinizi giriniz."))
        if kullanici2Bahis>kullaniciBakiye2:
            print("İkinci oyuncunun bahisi, bakiyesini aşmaktadır.")
            continue
        kullaniciBakiye1-=kullanici1Bahis
        kullaniciBakiye2-=kullanici2Bahis
        havuz=kullanici1Bahis+kullanici2Bahis
        break

    while True:
        oyuncu1Zar = r(1,6)
        oyuncu2Zar = r(1,6)
        print("Birinci oyuncunun zarı => {}".format(oyuncu1Zar))
        print("İkinci oyunucunun zarı => {}".format(oyuncu2Zar))
        if oyuncu1Zar>oyuncu2Zar:
            kullaniciBakiye1+=havuz
            print("Tebrikler!! Birinci oyuncu kazandı. Kazanılan tutar => {}, Birinci oyuncu güncel bakiyesi => {}".format(havuz,kullaniciBakiye1))
            havuz = 0
            break
        elif oyuncu1Zar<oyuncu2Zar:
            kullaniciBakiye2+=havuz
            print("Tebrikler!! İkinci oyuncu kazandı. Kazanılan tutar => {}, İkinci oyuncu güncel bakiyesi => {}".format(havuz,kullaniciBakiye2))
            havuz = 0
            break
        elif oyuncu1Zar==oyuncu2Zar:
            print("Oyun berabere, zarlar tekrar atılacak")
            continue
    if kullaniciBakiye1<=0:
        print("Birinci oyuncu iflas ettiği için oyun sona ermişir.")
    elif kullaniciBakiye2<=0:
        print("İkinci oyuncu iflas ettiği için oyun sona ermiştir.")
