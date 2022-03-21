# Parametre olarak aldığı listedeki tek elemanları yazdıran
# fonksiyonu yazınız.

def ListeyiYazdir(liste):
	for i in liste:
		if str(i).isdigit() and i%2 ==1:
			print(i)

listem =  {1,2,3,4,5, "Ahmet", "Burak",True}

ListeyiYazdir(listem)