## DEGER DONDUREN FONKSİYONLAR ##
#
# kare = pow(4,2)
# print(kare)

def usAl(taban, us):
	sonuc = taban ** us
	return sonuc


cebimdekiPara = usAl(10, 2)

print(cebimdekiPara)


# Bir müşterim dolar'ını euro'ya çevirmek istiyor
# ben dolar/euro endeksini bilmediğim için doları tl => tl euro

def dolar_to_tl(dolar):
	return dolar * 14.60


def tl_to_euro(tl):
	euro = tl / 16.36
	print(euro)


dolar = int(input("Kaç dolar bozduracaksınız ?"))

turkParasi = dolar_to_tl(dolar)
print(turkParasi)
tl_to_euro(turkParasi)
