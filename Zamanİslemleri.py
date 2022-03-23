from datetime import datetime
import locale

zaman = datetime.now()
print(zaman)  ## YYY-AA-GG  SA-DK-SN.SALISE

print(zaman.year)
print(zaman.month)
print(zaman.day)
print(zaman.fold)

dogumTarihim = datetime(1993, 11, 20)
print(dogumTarihim)
"""
%d  : rakam ile gün
%m  : rakam ile ay
%Y  : rakam ile 4 haneli yıl
%y  : rakam ile 2 haneli yıl
%b  : yazı ile 3 haneli ay
%H  : rakam ile saat 
%M  : rakam ile dakika 
%S  : rakam ile saniye 
%a  : yazı ile 3 haneli gün
%A  : yazı ile tam gün adı
%D  : AY/GUN/YIL
"""

print("Doğum Tarihim : ", dogumTarihim.strftime("%d.%m.%Y"))

locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
bugun = datetime.now()
print(bugun.strftime("%A"))

# YIL-AY-GUN--Saat:Dakika:Saniye--GünAdı

zaman = datetime.now()
print(zaman.strftime("%Y-%m-%d--%H:%M:%S--%A"))

zamanStr = "2022-03-23--20:02:36--Çarşamba"

zList = zamanStr.split("--")

print(zList[0].split("-"))
print(zList[1].split(":"))
print(zList[2])
