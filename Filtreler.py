##### FILTER #####
'''
sayılabilen (iterable) tipindeki değerlerin içindeki , item'ları
süzme işlemi yapar ve sadece True deger donduren sonuçları verir.
Verdiği sonucun tipi filter tipindedir. Bunu list veya tuple
çevirmemiz gereklidir. Döngülere göre hız olarak daha başarılıdır.
'''

liste = [12, 32, 44, 11, 12345, 6543, 213234]
# cc = []
# for item in liste:
#     if item %2==0:
#         cc.append(item)
#
# print(cc)

# stream api

dd = list(filter(lambda sayi: sayi % 2 == 0, liste))
print(dd)

dd = list(filter(lambda sayi: sayi % 2 == 1, liste))
print(dd)

ifade = "rakam123evethayir"
# ('r','a','k','a','m' ...
rakamlar = tuple(filter(lambda x: str(x).isdigit(), ifade))

print(rakamlar)
liste = [6, 1, 8, 11, -5, 5, 9]
print([x for x in liste if x < 9 and x >= 5])

# x=lambda a,b: a if a>b else b