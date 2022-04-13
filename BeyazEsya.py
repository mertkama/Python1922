class BeyazEsya:

    def __init__(self):
        self.Marka = str()
        self.Model = ""
        self.EnerjiSinifi = ""
        self.Renk = ""
        self.Fiyat = 0.0
        self.UretimYili = 0

    def BilgiYazdir(self):
        print(f"""
                Marka           {self.Marka}
                Model           {self.Model}
                Enerji Sınıfı   {self.EnerjiSinifi}
                Renk            {self.Renk}
                Fiyatı          {self.Fiyat}
                Üretim Yılı     {self.UretimYili}
""")

    def BilgiYazdir(self, text):
        print(text)
