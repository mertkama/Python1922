# Try catch  - exception


# try:
#     sayi = int(input("Lütfen sayı gir"))
# except:
#     print("Lütfen sayı gir !")


# while True:
# while True:
#     try:
#         sayi1 = int(input("Bir sayı giriniz"))
#         break
#     except ValueError:
#         print("Girilen değer convert edilemedi...")
#     except MemoryError:
#         print("Bilgisayarınızda yeterli bellek alanı bulunmamaktadır.")
#     except ZeroDivisionError:
#         print("Sayı 0 a bölünemez")
#     except ImportError:
#         print("Modül dahil edilemedi")
#     except OverflowError:
#         print("Değişkenin kapasitesi aşıldı.")
#     except IndexError:
#         print("Koleksiyon index uzunluğu dışında bir değer girildi.")
#     except:
#         print("Geri kalan hata durumları için...")


# try:
#     sayi1 = int(input("Birinci sayı "))
#     sayi2 = int(input("İkinci sayı "))
#     bolum = sayi1 / sayi2
#     print(bolum)
# except ZeroDivisionError:
#     print("Sayı sıfıra bölünemez ")


# raise hata fırlatma
# not1 = int(input("Vize notunuzu giriniz"))
#
# if not1 < 0  or not1 > 100:
#     print("Hatalı giriş")
#     raise OverflowError("Not hatalı girildi")


#
# eposta =  input("Mail adresi")
# assert eposta =="info@mehmetnuri.net"

####### ALIŞTIRMALAR #########
# Kullancıdan 2 sayı 1'de işlem alıp önceden tanımladığınız methodlara alınan değerleri göndereceğiz.
# işlem topla,çıkar,çarp ve böl'den birisi değilse assert fırlatsın,
# Kullanıcıdan veri alınırken ValueError verdiğinde tekrar veri istensin
# ZeroDivisionError için tekrar veri istenmesin!

# def topla(s1, s2):
#     return s1 + s2
#
# def cikar(s1, s2):
#     return s1 - s2
#
# def carp(s1, s2):
#     return s1 * s2
#
# def bol(s1, s2):
#     return s1 / s2
#
#
# def IslemYap():
#     s1 = int(input("Birinci sayı"))
#     s2 = int(input("İkinci sayı"))
#
#     islem = input("Lütfen işlemi girin (topla,çıkar,çarp,böl): ")
#     assert islem == "topla" or islem == "çıkar" or islem == "çarp" or islem == "böl"
#
#     if (islem == "topla"):
#         print(topla(s1,s2))
#     elif(islem == "çıkar"):
#         print(cikar(s1,s2))
#     elif(islem == "çarpma"):
#         print(carp(s1,s2))
#     elif(islem == "böl"):
#         print(bol(s1,s2))
#
# #exception
#
# try:
#     IslemYap()
# except ValueError:
#     IslemYap()
#     print("Değer yanlış formatta girildi")
# except ZeroDivisionError:
#     print("Sayı  sıfıra bölünemez")
#     IslemYap()
# except:
#     print("Hata oluştu")


import datetime

# dd = open("log.txt", "a", encoding="utf-8")
#
# while True:
#     try:
#         sayi = int(input("Sayı:"))
#         print(sayi * 2)
#         print(sayi / 0)
#     except Exception as e:
#
#         print("{} -> {} Hatası".format(datetime.datetime.now().strftime("%Y.%m.%d %H:%M"), e.__class__.__name__),
#               file=dd)
#         break

from  HataYakala import Kontrol

Kontrol("sad")