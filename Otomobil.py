from Arac import Arac


class Otomobil(Arac):

    def __init__(self):
        super().__init__()
        self.KasaTipi = "Sedan"
        self.VitesTipi = "Otomatik"

    def BilgiYazdir(self):
        super().BilgiYazdir()
        print(f"""
            Kasa Tipi       :     {self.KasaTipi}
            Vites Tipi      :     {self.VitesTipi}
        """)

