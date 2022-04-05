class Insan():
    ad = ""
    soyad = ""

    @classmethod
    def konus(cls, insan):
        print(f"Ad: {insan.ad} Soyad : {insan.soyad}")

    def konusma(self):
        print(f"AD: {self.ad}, Soyad: {self.soyad}")

    @classmethod
    def Yazdir(cls, liste):
        for i in liste:
            print(i.ad, i.soyad)

    @classmethod
    def kaydet(cls, liste):
        a = Insan()
        a.ad = input("Bebeğin adı: ")
        a.soyad = input("Bebeğin soyadı")
        liste.append(a)


# a =  Insan()
# a.ad =  input("Bebeğin Adı")
# a.soyad =  input("Bebeğin Soyadı")
#
# Insan.konus(a)
# a.konusma()

# Liste = list()
# for i in range(3):
#     a = Insan()
#     a.ad = input("Bebek adı")
#     a.soyad = input("Bebek soyad")
#     Liste.append(a)
#
# Insan.Yazdir(Liste)

Liste = list()
while True:
    a = Insan()
    a.ad = input("Bebeğin Adı:")
    a.soyad = input("Bebeğin Soyadı:")
    Liste.append(a)
    cevap=input("Devam Mı? E/H")
    if(cevap.upper()=="H"):
        break

Insan.kaydet(Liste)
Insan.Yazdir(Liste)
