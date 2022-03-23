"""
Dosya Yetki Modları
w:  sadece yazma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r:  sadece okuma yetkisi ile açar.
a:  sona ekleme yetkisi ile açar. (dosya yoksa oluşturur.)
x:  yazma yetkisi ile açar. (yoksa oluşturur. varsa hata verir.)

w+: yazma + okuma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r+  okuma + yazma yetkisi ile açar.
a+  ekleme + okuma yetkisi ile açar. (dosya yoksa oluşturur.)
"""

import os

# os.chdir("C:\\TEST\\2022-03-23")
#
# dosyaAdres =  "C:\\TEST\\2022-03-23\\kare.doc"
# dosya = open(dosyaAdres, "w")
#
# print(type(dosya))
#
# for i in range(1,11):
#     dosya.write(str(i)+ "sayısının karesi: " + str(i**2) +"\n")
# dosya.close()


dosyaAdres = "C:\\TEST\\"
if (not os.path.exists(dosyaAdres)):
    os.mkdir(dosyaAdres)

dosyaAdres = dosyaAdres + "kare.csv"
dosya = open(dosyaAdres, "w")
for i in range(1, 11):
    dosya.write(str(i) + " sayısının karesi: " + str(i ** 2) + "\n")
dosya.close()

