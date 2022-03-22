# SORU: Kullanıcıdan 2 sayı 1 işlem alalım ve
# alınan sayılara verilen işlemi uygulayan ve
# ekrana yazdıran fonksiyonu yazınız.

def Hesapla(sayi1, sayi2, islem):
	if islem == "+":
		print(sayi1 + sayi2)
	elif islem == "-":
		print(sayi1 - sayi2)
	elif islem == "/":
		if sayi2 == 0:
			print("Sayı sıfır a bölünemez")
		else:
			print(sayi1 / sayi2)
	elif islem == "*":
		print(sayi1 * sayi2)
	else:
		print("Girilen işlem uygunsuz")


while True:
	cevap = input("İşleme devam etmek istiyor musunuz? (E/H)").upper()
	if cevap == "E":
		sayi1 = int(input("Lütfen birinci sayıyı giriniz : "))
		sayi2 = int(input("Lütfen ikinci sayıyı giriniz : "))
		islem = str(input("Lütfen işlem seçiniz : "))
		Hesapla(sayi1, sayi2, islem)
	else:
		break
