class Calisan():
    _personel = []

    def __init__(self, isim):
        self._isim = isim
        self.personel_ekle()

    def personel_ekle(self):
        self._personel.append(self._isim)
        print("{} adlı kişi personel listesine eklendi".format(self._isim))

    @classmethod
    def personelleri_gorutule(cls):
        print("PERSONEL LİSTESİ")
        for personel in cls._personel:
            print(personel)

    @property
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self, value):
        kisi = self._personel.index(self.isim)
        self._personel[kisi] = value
        print("Yeni İsim : ", value)


calisan1 = Calisan("ALi")
calisan1.personelleri_gorutule()
calisan1.isim =  "Veli"


