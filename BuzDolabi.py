from BeyazEsya import BeyazEsya


class BuzDolabi(BeyazEsya):

    def __init__(self):
        super().__init__()
        self.KapakSayisi = 0
        self.Hacim = 0
        self.En = 0
        self.Boy = 0
        self.Ozellik = ""

    def BilgiYazdir(self):
        super().BilgiYazdir()
        print(f"""
                    Kapak Sayısı           {self.KapakSayisi}
                    Hacim                  {self.Hacim}
                    En                     {self.En}
                    Boy                    {self.Boy}
                    Özellik                {self.Ozellik}
        """)

    def Kaydet(self):
        dizin = "C:\\Test\\OOP4\\"
        dosya = dizin + "BuzDolabi.txt"

        import os

        if not os.path.exists(dizin):
            os.mkdir(dizin)
            print(f" {dizin}  dizini oluşturuldu")

        if not os.path.exists(dosya):
            text = open(dosya, "a+")
            text.write("Marka\t\tModel\t\tEnerji Sınıfı\t\tKapak Sayısı\t\tHacim\n")
            text.write("--------\t\t--------\t\t--------\t\t--------\t\t--------\n")
        else:
            text = open(dosya, "a+")

        text.write(f"""{self.Marka}\t\t{self.Model}\t\t{self.EnerjiSinifi}\t\t{self.KapakSayisi}\t\t{self.Hacim}""")
        text.close()
