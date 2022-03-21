# Kendisine parametre olarak gönderilen sayının
# faktöriyelini hesaplayıp döndüren fonksiyonu yazınız.

# 3! =  3*2*1

# def faktoryel_hesaplama(sayi):
# 	carpim = 1
# 	for s in range(1, sayi + 1):  # => 1,2,3,4,5
# 		carpim *= s
# 	return carpim
#
#
# sonuc = faktoryel_hesaplama(5)
# print(sonuc)


# Kendisine gönderilen sayının asal olup olmadığını döndüren fonksiyonu yazınız.
# Asalsa: True değilse: False
# Asal sayı :1 ve kendisi hariç hiç bir sayıya bölünemeyen sayıdır. 2 en küçük asal sayıdır. 13 7 17

def sayiAsalMi(sayi):
	if (sayi == 1):
		return False
	elif (sayi == 2):
		return True
	for i in range(2, sayi):
		if sayi % i == 0:
			return False
	return True

if(sayiAsalMi(17)):
	print("Sayı asal")
else:
	print("Asal değil")