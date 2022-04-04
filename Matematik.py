class Matematik:

    @classmethod
    def topla(cls, *sayilar):
        toplam = 0
        for sayi in sayilar:
            toplam += int(sayi)
        print(toplam)

    @classmethod
    def cikar(cls, s1, s2):
        print((s1 - s2))

    @classmethod
    def carp(cls, *sayilar):
        carpim = 1
        for i in sayilar:
            carpim *= i
        print(carpim)

    @classmethod
    def bol(cls, s1, s2):
        try:
            bolum = s1/s2
            print(int(bolum))
        except ZeroDivisionError:
            print("Sıfıra bölme yapılamaz")
        except:
            print("Bölme işleminde hata oluştu")


Matematik.topla(5, 6, 5, 5, 12)
Matematik.cikar(10, 5)
Matematik.carp(1, 2, 3, 4, 5)
Matematik.bol(1,1)
