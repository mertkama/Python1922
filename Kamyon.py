from Arac import Arac


class Kamyon(Arac):

    def __init__(self):
        super().__init__()
        self.TasimaKapasitesi = "3 Ton"
        self.YakitDepoSayisi = 1


    def BilgiYazdir(self):
        super().BilgiYazdir()
        print(f"""
                           Taşıma Kapasitesi        :     {self.TasimaKapasitesi}
                           Yakıt Depo Sayısı        :     {self.YakitDepoSayisi}
               """)
