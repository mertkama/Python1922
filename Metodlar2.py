# Obeb hesaplama
def ObebHesapla(s1, s2):
    obeb = 1
    for i in range(2, min(s1, s2) + 1):
        if s1 % i == 0:
            obeb = i
    return obeb


# print(ObebHesapla(60, 100))


# (s1 * s2)/obeb

def OkekHesapla(s1, s2):
    obeb = ObebHesapla(s1, s2)
    okek = (s1 * s2) / obeb

    return okek
    # print("Okek : {}, Obeb {}".format(okek,obeb))


# OkekHesapla(30,65)

def kullanicidan_bilgial():
    sayi1 = int(input("Lütfen 1. sayıyı giriniz"))
    sayi2 = int(input("Lütfen 2. sayıyı giriniz"))
    obeb = ObebHesapla(sayi1, sayi2)
    okek = OkekHesapla(sayi1, sayi2)

    print("Obeb {},  Okek {}".format(obeb, int(okek)))


kullanicidan_bilgial()