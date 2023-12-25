import random;

sayi = random.randint(0, 30)

while True:

    tahmin = input("Bir sayı giriniz: ")
    tahmin = int(tahmin)

    if tahmin < sayi:
        print("Daha büyük")
    elif tahmin == sayi:
        print("Tebrikler doğru sayıyı buldunuz.")
        break
    elif tahmin > sayi:
        print("Daha küçük")
