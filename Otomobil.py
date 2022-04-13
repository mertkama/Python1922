class Otomobil:

    def __init__(self, marka, model, renk, motor_hacmi, uretim_yili):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.motor_hacmi = motor_hacmi
        self.uretim_yili = uretim_yili

    def kaydet(self):
        import os, datetime

        dizin = "C:\\Test\\"
        if not os.path.exists(dizin):
            os.mkdir(dizin)

        dosya = dizin + str(datetime.date.today()) + ".txt"  #C:\Test\GününTarihi.txt
        acik_dosya = open(dosya, "a")

        acik_dosya.write("\nMarka:" + str(self.marka) + "\nModel:" + str(self.model) + "\nRenk:" + str(self.renk)
                         + "\nMotor Hacmi:" + str(self.motor_hacmi) + "\nÜretim Yılı:" + str(self.uretim_yili))

        acik_dosya.close()
