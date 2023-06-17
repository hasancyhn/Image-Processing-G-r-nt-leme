# Bu tek satirlik yorumdur
"""
Bu coklu yorum blogudur.
Birden fazla satirdan olusur.
"""

a = 3
b = 16
c = b/a
d = b//a
e = a**2
print(c)
print(d)
print(e)
print("Goruntu islemeye giris")
print('Goruntu islemeye giris')
print('Murat Karakoyun\'a Mektup')
print("Goruntu" + "Isleme")
print("Goruntu", "Isleme")
print("Goruntu", "Isleme", sep="-")
print("Goruntu", "Isleme", sep="-", end=":Murat Karakoyun\n")
print("Goruntu Isleme Ortalamasi: ", e)
print("Goruntu Isleme Ortalamasi: ", str(e))

"""
dersAdi  = input("\nDers adi giriniz: ")
dersNotu = int(input("Puaninizi giriniz: "))
dersNotu = dersNotu*2
print("Ders: ", dersAdi, "Puan: ", dersNotu)
"""

str1 = "kare"
str1 = str1*2
print("\n" + str1)
print("Ilk karakter: ", str1[0])
print("String boyutu: ", len(str1))
print("Aralik: ", str1[1:4])

dersler = ["Algoritmalar", "Veritabani", "Goruntu ısleme"]
print("\n",dersler)
dersler = dersler + ["Tarih"]
print(dersler)
dersler.append("Cografya")
print(dersler)
notlar = [10, 20, 30, 40]
print(notlar)

dersVePuanlar = ["Algoritma", 85, "Veritabani", 100]
print("\n", dersVePuanlar)
print(dersVePuanlar[0] + ":", dersVePuanlar[1])
print(len(dersVePuanlar))

sozlukYapisi = {"1":"Algoritmalar", "2":"Veritabani"}
print("\n", sozlukYapisi)
sozlukYapisi = {"1":"Algoritmalar", "2":"Veritabani", "2":"Tarih"}
print(sozlukYapisi)

"""
# Sartli Ifadeler: if-elif
sayi1 = int(input("\nIlk Sayiyi Giriniiz: "))
sayi2 = int(input("Ikinci Sayiyi Giriniiz: "))

if sayi1 > sayi2:
    print("Buyuk Sayi: ", sayi1, "\n")
elif sayi1 < sayi2:
    print("Buyuk Sayi: ", sayi2, "\n")
else:
    print("Sayilar Esittir.\n")
"""

# Donguler: for-while
notlar = [50, 60, 70, 80, 90, 100]
for i in notlar:
    print(i)
print("\n")

# range() Fonksiyonu
sayiSiralamasi = range(1, 30, 1)
for i in sayiSiralamasi:
    if i % 4 == 0 and i % 7 == 0:
        print(i, "\n")
        break
for i in sayiSiralamasi:
    if i % 2 == 0:
        continue
    print(i)
print("\n")

# Sonsuz dongu
x = 1
while True:
    if x % 5 != 0:
        print(x)
    else:
        break
    x = x + 1
print("\n")

# Fonksiyonlar
def toplama(say1, say2):
    toplam = say1 + say2
    return toplam
    # print(toplam)
a = 10
b = 20
# toplama(a, b)
t = toplama(a, b)
print("Toplam: ", t)
print("\n")

# Default degerli fonksiyon tanimlama
def faktoriyel(sayi=1):
    f = 1
    i = 1
    while i <= sayi:
        f = f*i
        i = i+1
    return f
f = faktoriyel(5)
print("Faktoriyel Sonucu: ", f)