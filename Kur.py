import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Veritabani import Veritabani


class Kur:

    @staticmethod
    def Getir(doviz_tipi):
        driver =  "C:\\Users\\1\\PycharmProjects\\DovizTakip\\chromedriver.exe"
        opsiyonlar =  Options()
        opsiyonlar.add_argument("--headless")
        browser = webdriver.Chrome(executable_path=driver, options=opsiyonlar)
        browser.get("https://www.haberturk.com/")

        if(doviz_tipi == "altin"):

            icerik =  browser.find_element_by_css_selector("a#gram-altin span:nth-child(2)").text

        if (doviz_tipi == "dolar"):
            icerik = browser.find_element_by_css_selector( "a#dolar span:nth-child(2)" ).text

        if(doviz_tipi == "euro"):
            icerik = browser.find_element_by_css_selector( "a#euro span:nth-child(2)" ).text


        deger = float(icerik.replace(",", "."))

        tablo =  "tb_"+ str(doviz_tipi)

        zaman = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print(zaman)

        komut =  f"Insert Into {tablo} (zaman, kur) values( '{zaman}', '{deger}')"
        Veritabani.Kaydet(komut)
