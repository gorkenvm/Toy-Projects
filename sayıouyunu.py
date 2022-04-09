import random
random_sayi = round(random.random()*100)

sayi = int(input("0-100 arasi sayi giriniz"))
while sayi != random_sayi:
    if sayi > random_sayi:
        print("Büyük girdiniz")
    else:
        print("Küçük girdiniz")
    sayi = int(input("0-100 arası sayı giriniz"))
print("Tebrikler Kazandınız")
