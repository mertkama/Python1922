from  Matematik import Matematik

class Araba:
    kapiSayisi = 0
    rengi = ""
    pencereSayisi = 0
    modeli = ""
    marka = ""

    def bilgiver(self):
        print(
                f"Kapı Sayısı:{self.kapiSayisi}  Renk:{self.rengi} PencereSayısı:{self.pencereSayisi} Model:{self.modeli}"
                f" Marka:{self.marka}")

    @classmethod
    def Arama(cls, Marka, liste):
        for i in liste:
            if (i.marka == Marka):
                print(f"Kapı Sayısı:{i.kapiSayisi}  Renk:{i.rengi} PencereSayısı:{i.pencereSayisi}"
                      f" Model:{i.modeli} Marka:{i.marka}")


bmwi8 = Araba()  # instance
bmwi8.kapiSayisi = 2
bmwi8.marka = "BMW"
bmwi8.rengi = "Kırmızı"
bmwi8.pencereSayisi = 6
bmwi8.modeli = "i8"

audia8 = Araba()
audia8.kapiSayisi = 4
audia8.marka = "AUDI"
audia8.rengi = "Siyah"
audia8.pencereSayisi = 6
audia8.modeli = "A8"

audia8.bilgiver()

liste = {bmwi8, audia8}

Araba.Arama("BMW", liste)

Matematik.bol(12,3)