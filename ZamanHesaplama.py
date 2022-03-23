# from datetime import timedelta, date, datetime
import  datetime
# bugun = datetime.now()
# print(bugun)
#
# dogumTarihi = datetime(1993, 11, 20)
# print(dogumTarihi)
#
# birHaftaOnce = bugun - timedelta(7)
# print(birHaftaOnce)

bugun = datetime.datetime.now()
print(bugun)
dogumTarihi = datetime.datetime(1993, 11, 20)
print(dogumTarihi)

print(bugun-(datetime.timedelta(dogumTarihi)))
