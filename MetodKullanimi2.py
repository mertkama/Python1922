# SORU: Kendisine gönderilen sayı adedince
# klavyeden girilen ismi alıp listeye atan fonksiyonu yazınız.

def IsimYaz():
	isimListesi = list()
	sayi = int(input("Lütfen kaç adet isim girmek istedinizi belirtin: "))
	for i in range(sayi):
		isim = input("İsim: ")
		isimListesi.append(isim)
	print(isimListesi)

IsimYaz()

listem = list()
def IsimYaz2(name):
	listem.append(name)

sayi = int(input("Kaç adet isim girilecek"))

for i in range(sayi):
	isim = input("İsim")
	IsimYaz2(isim)
	
print(listem)
