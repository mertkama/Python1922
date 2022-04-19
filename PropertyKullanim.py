# class Celcius:
#
#     def __init__(self, sicaklik=0):
#         self.sicaklik = sicaklik
#
#     def fahrenayt(self):
#         return (self.sicaklik * 1.8) + 32
#
# n01 =  Celcius(40)
# print(n01.fahrenayt())
# print(n01.sicaklik)

# class Celcius:
#
#     def __init__(self, sicaklik=0):
#         self.set_sicaklik(sicaklik)
#
#     # Get Bölümü
#     def get_sicaklik(self):
#         return self.__sicaklik
#
#     # Set Bölümü
#     def set_sicaklik(self, deger):
#         if deger < -273:
#             raise ValueError("Sıcaklık -273 den küçük olamaz")
#
#         self.__sicaklik = deger
#
#     def fahrenayt(self):
#         return (self.sicaklik * 1.8) + 32
#
#
# n02 = Celcius(-270)
# print(n02.get_sicaklik())


# class Celcius:
#
#     def __init__(self, sicaklik=0):
#         self.sicaklik = sicaklik
#
#     # Get Bölümü
#     def get_sicaklik(self):
#         return self.__sicaklik
#
#     # Set Bölümü
#     def set_sicaklik(self, deger):
#         if deger < -273:
#             raise ValueError("Sıcaklık -273 den küçük olamaz")
#
#         self.__sicaklik = deger
#
#     def fahrenayt(self):
#         return (self.sicaklik * 1.8) + 32
#
#
#     sicaklik = property(get_sicaklik, set_sicaklik)
#
# n03 = Celcius(-77)
# print(n03.sicaklik)
# print(n03.fahrenayt())


class Celcius:

    def __init__(self, sicaklik=0):
        self.__sicaklik = sicaklik

    def fahrenhayt(self):
        return (self.sicaklik * 1.8) + 32

    @property
    def sicaklik(self):
        print("Değer döndürülüyor")
        return self.__sicaklik

    @sicaklik.setter
    def set_sicaklik(self, deger):
        print("Değer alınıyor")
        if deger < -273:
            raise ValueError("Sıcaklık 273 altı olamaz")
        self.__sicaklik = deger


n03 = Celcius(-77)
print(n03.sicaklik)
print(n03.fahrenhayt())
