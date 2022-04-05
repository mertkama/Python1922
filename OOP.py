###################################################################
############### OOP: Object Oriented Programming ##################
################ Nesneli Yöneliklik Programlama ###################
###################################################################

"""
ad = "Mehmet"
soyad = "Öztürk"
tc = 44
dogumTarihi = "20.11.1993"


ad1 = "Ali"
soyad1 = "Öztürk"
tc1 = 45
dogumTarihi1 = "25.10.1989"

"""


class Ogrenci:
    # Sınıf Nitelikleri(Özellikleri)
    adi = ""
    soyad = str()
    tc = ""
    dogumTarihi = ""
    numara = 0

    def BilgiListele(self):
        print("********************* ÖĞRENCİ BİLGİLERİ *********************")
        print(f"Öğrenci Adı: {self.adi}, Soyadı: {self.soyad}, {self.tc},"
              f"  {self.dogumTarihi}, {self.numara}")


a = Ogrenci() #nesnem => a #instance işlemi,
a.adi = "Mehmet"
a.soyad = "Öztürk"
a.dogumTarihi = "20.11.1993"
a.tc = 123
a.numara = 44
a.BilgiListele()



