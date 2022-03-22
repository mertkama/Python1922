### Bir fonksiyon içinde fonksiyon çağrılması

def buyuk2(a, b):
	if (a > b):
		return a
	elif (b > a):
		return b
	else:
		return a


def buyuk3(x, y, z):
	return buyuk2(x, buyuk2(y, z))  # => buyuk(x,y)


print(buyuk3(3, 4, 5))
