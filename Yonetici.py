from Calisan import Calisan


class Yonetici(Calisan):

    def zamYap(self,zam_miktari):
        self.maas += zam_miktari


### OVERRIDING (iptal Etme-Revize)

    def bilgiGoster(self, metin):
        print("Yönetici sınıfının bilgi goster metodu çalıştı")
        print(f"İsim:\t{self.isim}\n Maaş:\t{self.maas} ")
