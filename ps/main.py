import random
import string
from time import sleep

print(" ")

metin = "-----> Welcome to Password Generator <-----"
metin1 = "> created by.nowte <"
genislik = 77
genislik1 = 53

metin_uzunlugu = len(metin)
bosluk_sayisi = genislik - metin_uzunlugu

print(metin.rjust(genislik // 2 + metin_uzunlugu))
print(metin1.rjust(genislik1 // 2 + metin_uzunlugu))

sleep(3)
print("Wait...")
print(" ")
sleep(2)
print("Application is Ready!")
sleep(3)
print(" ")

while True:
    def sifre_olustur(uzunluk):
        sifre_karakterleri = string.ascii_letters + string.digits + string.punctuation
        sifre = "".join(random.choice(sifre_karakterleri) for i in range(uzunluk))
        return sifre


    while True:
        sifre_uzunlugu = int(input("Enter Password Length: "))
        sifre = sifre_olustur(sifre_uzunlugu)
        print(" ")
        print(f"Generated Password: {sifre}")
        print(" ")
        devam = input("Would you like to create a password again? (y|yes/n|no): ")
        print(" ")
        if devam.lower() == ("y", "yes"):
            break

        elif devam == ("n", "no"):
            print("Application Closing...")
            sleep(2)
            print(metin1.rjust(genislik1 // 2 + metin_uzunlugu))
            sleep(5)
            exit()
while True:
    pass