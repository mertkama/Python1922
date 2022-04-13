############## KALITIM-INHERITANCE ###############
from Calisan import Calisan
from Yonetici import Yonetici

c =  Calisan("Mehmet", "3255", "AR_GE")
c.bilgiGoster()


y =  Yonetici("Ali", 5655, "IT")
y.bilgiGoster()
y.departman_degistir("Sistem",y)
y.bilgiGoster()

y2 =  Yonetici("Kemal", 5000, "Grafiker")
y2.zamYap(300)
print(y2.maas)

y3 =  Yonetici("Kazim", 10000,"Yazılım")
y3.bilgiGoster()