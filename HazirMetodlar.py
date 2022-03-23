"""
Hazır String Fonksiyon(Metod)lar

capitalize() İlk karakteri büyük harfe çevirir.
count()      Bir dizide belirtilen değerin kaç defa gerçekleştiğini döndürür.
endswith()   Dize belirtilen değer ile bitmiş ise true döndürür.
find()       Dizede belirli bir değeri arar ve bulunduğu yeri döndürür.
format()     bir dizede belirtilen değerleri formatlar.
index()
isalpha()    Dizedeki bütün karakterleri alfabede ise True döndürür.
isdecimal()  Dizedeki bütün karakterler ondalıksa True döndürür.
isdigit()
islower()
isupper()
isnumeric()
isspace()    Dizede boşluk varsa True döndürür.
ljust()      Dizeyi sola dayalı bir sürüm döndürür.
rjust()
lstrip()     Dizenin sol tirm versiyonunu döndürür.
rstriip()
strip()
replace()
split()      Dizeyi belirtilen ayrıcıya böler.
isalnum()    Dizedeki değerler Alfabe ve numara olması durumunda True döner


"""

metin = "    Mehmet Nuri    "

print(metin.lstrip())
print(metin.rstrip())
print(metin.strip())

# Kelime Parçalama
kelime = "Bu.gün.hava.çok.soğuktu"
print(kelime.split("."))
kelime = kelime.split(".", 3)
print(kelime)

# Alfabetik Kontrol
metin = "Bu gun  3 maç kazandık"

if metin.isalpha():
    print("Bu metinde sayı yok")
else:
    print("Bu metinde sayı var")

#Metin sayısal karakterlerden mi oluşuyor ?
metin = "12146546876468"
if metin.isalnum():
    print("Sadece sayılar var")
else:
    print("Sayı karakter karışık")
