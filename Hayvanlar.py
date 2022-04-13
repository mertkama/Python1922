class Hayvanlar:
    def __init__(self, isim):
        self.isim = isim


class Kedi(Hayvanlar):

    def Tepki(self):
        return "Miav"


class Kopek(Hayvanlar):

    def Tepki(self):
        return "Hav hav"


hayvanlar = [Kedi("Boncuk"), Kopek("Paşa"), Kedi("Minnak"), Kopek("Dobi")]

for hayvan in hayvanlar:
    print(hayvan.isim , hayvan.Tepki())
