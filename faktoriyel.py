
# Herhangi bir modül kullanmadan kullanıcı tarafından girilen sayının faktoriyeli;

sayi = int(input("Lütfen faktoriyelini almak istediğiniz sayıyı giriniz: "))

faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i
print(faktoriyel)


######Fonksiyon#####

def factor(number):
    factorial = 1
    for x in range(1, number + 1):
        factorial *= x
    print(factorial)


factor(5)
