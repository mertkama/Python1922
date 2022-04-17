from Kamyon import Kamyon
from Otomobil import Otomobil

fordFocus = Otomobil()
fordFocus.Marka = "Ford"
fordFocus.Model = "2021"
fordFocus.Uretim_Yili = 2020
fordFocus.Renk = "Siyah"
fordFocus.Fiyat = 400000.0
fordFocus.KasaTipi = "HP"
fordFocus.VitesTipi = "Manuel"

fordFocus.BilgiYazdir()


print("**********************")
kamyon=Kamyon()
kamyon.Marka="Mercedes"
kamyon.Model="Actros"
kamyon.TasimaKapasitesi=50000
kamyon.Fiyat=600000
kamyon.UretimYili=2018
kamyon.Renk="Mavi"
kamyon.YakitDepoSayisi=2
kamyon.BilgiYazdir()