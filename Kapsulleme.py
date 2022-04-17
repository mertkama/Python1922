class Kapsul:

    def __init__(self):
        self.__gizliOzellik = "Varsayılan Değer"
        self.__gizliOzellik2 = "Varsayılan Değer"

    def getGizli(self):
        return self.__gizliOzellik

    def setGizli(self, deger):
        self.__gizliOzellik = deger

    def getGizli2(self):
        return self.__gizliOzellik2

    def setGizli2(self, deger):
        if not (len(deger) < 1):
            self.__gizliOzellik2 = deger


k = Kapsul()
k.setGizli2("Mehmet")
print(k.getGizli2())
print(k.getGizli())
