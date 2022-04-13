# SORU:
"""
Personel isimli bir class tanımlayın
Nesne Nitelikleri: ad,soyad,tc,telefon,adres,maas
__init__ fonksiyonu ile kullanıcıdan bu özellikler sorularak doldurulsun

Kaydet() isimli method Personel.txt adında bir dosyaya kaydetsin
Bir tane sınıf üzerinden erişebilir Listele() adında bir method
tanılayın dosyadaki verileri okuma işlemi gerçekleştirsin

"""


class Personel:

    def __init__(self):
        print("Personel Bilgilerini Lütfen Giriniz : ")
        self.ad         = input("Personel Adı : ")
        self.soyad      = input("Personel Soyadı : ")
        self.tc         = input("Personel T.C. : ")
        self.telefon    = input("Personel Telefon: ")
        self.adres      = input("Personel Adres : ")
        self.maas       = input("Personel Maaş : ")

    def Kaydet(self):
        import  os

        dizin =  "C:\\Test\\"
        dosya = dizin +"Personel.txt"

        if not os.path.exists(dizin):
            os.mkdir(dizin)

        dosya =  open(dosya, "a")
        dosya.write(f"Ad :\t{self.ad}\nSoyad:\t{self.soyad}\nT.C.:\t{self.tc}\nTelefon:\t{self.telefon}\nAdres:\t{self.adres} "
                    f"\nMaaş:\t{self.maas}")
        dosya.close()

    @staticmethod
    def Listele():
        import os

        dosya ="C:\\Test\\Personel.txt"

        if not os.path.exists(dosya):
            print("Dosya Bulunamadı!")
            return
        else:
            with open(dosya, "r") as f:
                satilar =  f.readlines()

            for satir in satilar:
                print(satir)
            f.close()
