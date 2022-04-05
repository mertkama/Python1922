class Insan():

    def __int__(self):
        pass

    def __int__(self):
        print("Merhaba kurucu fonksiyon Çalıştı !")

    # def __init__(self, metin):
    #     print(metin)

    # def __init__(self, isim,soyisim):
    #     self.isim =  isim
    #     self.soyisim =  soyisim

    def __init__(self):
        self.InsanKaydet()

    def InsanKaydet(self):
        self.isim = input("Bebek Adı")
        self.soyisim = input("Soyad")

    @staticmethod
    def Topla(s1,s2):
        return  s1+s2


# insan = Insan()
#
# print(insan.isim)
# print(insan.soyisim)

print(Insan.Topla(5,6))
