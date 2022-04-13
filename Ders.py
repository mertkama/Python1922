class Ders:
    def __init__(self, ders_adi, ders_saati, ders_ogretmeni, ders_tarihi):
        self.ders_adi = ders_adi
        self.ders_saati = ders_saati
        self.ders_ogretmeni = ders_ogretmeni
        self.ders_tarihi = ders_tarihi
        self.ders_kaydet()

    def ders_kaydet(self):

        try:
            import os
            dizin = "C:\\Test\\Ders\\"
            kayit_dosyasi = dizin + "dersler.txt"  # C:/Test/Ders/dersler.txt

            if not os.path.exists(dizin):
                os.mkdir(dizin)

            dosya = open(kayit_dosyasi, "a")

            yazi = "\n" + "Ders Adı :\t" + str(self.ders_adi) + "\n" + "Ders Saati :\t" \
                   + str(self.ders_saati) + "\n" + "Ders Öğretmeni :\t" + str(self.ders_ogretmeni) \
                   + "\n" + "Ders Tarihi :\t" + str(self.ders_tarihi)

            dosya.write(yazi)
            dosya.close()
            print("Ders Başarıyla Kayıt Edildi !")
        except FileNotFoundError:
            print("Dosya Bulunamadı!")
        except IOError:
            print("Dosya Yazılırken Hata  Oluştu !")
        except OSError:
            print("Dosya okunamadı")
        except Exception as e:
            print("Beklenmedik Hata Oluştu ! " + e)
