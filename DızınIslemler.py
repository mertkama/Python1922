"""
getcwd()    => hangi dizinde olduğumuzu gösterir
system()    => Kullanırken çok dikkat edeceğimiz bir methoddur.
getcwd()    => Sistemin şuan işlem yaptığı dizin döndürülür.
chdir()     => Farklı bir dizine geçmemizi sağlar.
listdir()   => Bulunduğumuz dizinde mevcut dosyaları getirir.
mkdir()     => Bulunduğumuz dizinde yeni klasör açar.
rmdir()     => İçi boş olan bir klasörü siler.
rename()    => İsim değiştirir
path()      => Bir dosya veya klasörün var olup olmadığını kontrol
etmek istediğimizde path.exists() komutu kullanırız.
"""

from os import *
from datetime import *


# C:\Users\1\PycharmProjects\DizinDosyaIslemleri => Windows
# /home/mehmet/Projects/DizinDosyaIslemleri  => Linux & Mac

# chdir("C:\\")
# print(getcwd())
#
# for i in listdir():
#     print(i)
#
# mkdir(getcwd() + "TEST")


# def klasorVarmi(klasorYolu="C:\\TEST"):
#     return path.exists(klasorYolu)
#
# varmi = klasorVarmi()
# print(varmi)


# SORU1: C:\TEST\YIL-AY-GUN ismi ile bir klasör oluşturunuz


def bugununTarihiniStringOlarakVer():
    bugun = datetime.now()
    return bugun.strftime("%Y-%m-%d")

def klasoruOlustur():
    dosyaYolu =  "C:\\TEST\\"+bugununTarihiniStringOlarakVer()
    if not path.exists("C:\\TEST"):
        mkdir("C:\\TEST")

    if(not path.exists(dosyaYolu)):
        mkdir(dosyaYolu)
# 'C:\\TEST\\2022-03-23'

klasoruOlustur()