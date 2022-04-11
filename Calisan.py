class Calisan():

    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu çalıştı")
        self.isim =  isim
        self.maas =  maas
        self.departman =  departman


    def bilgiGoster(self):
        print("Çalışan sınıfının bilgileri....")
        print(f"İsim:\t{self.isim}\n Maaş:\t{self.maas}\
        n Departman:\t{self.departman}")

    @classmethod
    def departman_degistir(cls, yeni_departman, self):
        print("Departman Değiştiriliyor....")
        self.departman =  yeni_departman