# Acess Modifier public private protected
#
# class Muhendis:
#     ad ="Mehmet"
#     __soyad ="Öztürk"
#
#     def EkranaYaz(self):
#         print(self.ad)
#         print(self.__soyad)
#
#
# mehmet = Muhendis()
# mehmet.EkranaYaz()

# class Uye:
#     isim = ""
#     soyisim = ""
#     __tc = int()
#
#     def Kaydet(self):
#         self.isim = input("Adınız :")
#         self.soyisim = input("Soyadınız:")
#         TC = input("TC:")
#
#         if len(TC) == 11 and TC.isnumeric():
#             self.__tc = TC
#         else:
#             self.__tc = "00000000000"
#
#     def Yaz(self):
#         print(self.isim, self.soyisim, self.__tc)
#
#
# a =  Uye()
# a.Kaydet()
# a.Yaz()

#
# class Muhendis:
#     ad = "Mehmet Nuri"
#     soyad = "Öztürk"
#
#     def _EkranaYaz(self):
#         print(self.ad)
#         print(self.soyad)
#
#
# class Makine(Muhendis):
#
#     def __init__(self):
#         self._EkranaYaz()
#
#     pass
#
#
# muhendis = Muhendis()
# muhendis._EkranaYaz()
#
# makine = Makine()

