# def topla(sayi1, sayi2):
# 	toplam = sayi1+sayi2
# 	print(toplam)
#
# topla(1,2)

# def toplama(*sayilar): # * ifadesi n sayıda parametreyi ifade eder
# 	toplam = 0
# 	for i in sayilar:
# 		toplam += i
# 	print(toplam)
#
# toplama(1,2,3,5,4,4,545,54,5475)

# Kendisine gönderilen karakter,en,boy parametrelerine
# göre ekrana karakterden oluşan bir dikdörtgen oluşturan
# fonksiyonu yazınız.

def DikdortgenCiz(karakter, en, boy):
	for i in range(boy):
		print(karakter*en)

DikdortgenCiz('~', 30,10)