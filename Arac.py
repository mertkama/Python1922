class Arac:

    def __init__(self):
        self.Marka = str()
        self.Model = str()
        self.Renk = str()
        self.Uretim_Yili = 1900
        self.Fiyat = 0.0
        from datetime import datetime as dt
        self.Ilan_Tarihi = dt.today().date()

    def BilgiYazdir(self):
        print(f"""
            Marka       :     {self.Marka}
            Model       :     {self.Model}
            Renk        :     {self.Renk}
            Üretim Yili :     {self.Uretim_Yili}
            Fiyat       :     {self.Fiyat}
            İlah Tarihi :     {self.Ilan_Tarihi}
""")
