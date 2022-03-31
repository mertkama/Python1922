###### Map() ######
'''
iterable(sayılabilen) tipteki değişkenin içindeki
 elemanlara matematiksel işlem yapmaya yarar.
 Sorgu işlemi yapılamaz, yapılırsa True-False değer döner.

map(func,iter)
'''
#
# liste = [2, 3, 4]
#
#
# def karesiniAl(sayi):
#     return sayi ** 2
#
#
# # Map yokken
# kareler = []
# for i in liste:
#     kareler.append(karesiniAl(i))
#
# print(kareler)
#
# # Map geldiğinde
# sonuc = list(map(karesiniAl, liste))
# print(sonuc)


# Lambda ile map kullanımı
# dd = [1, 2, 3, 4, 5, 6, 7, 8]
# x = tuple(map(lambda x: x ** 2, dd))
# print(x)

dd = [1, 32, True, 234, 213, "1234", 34.567, 5, 734, 12]

# ints = list(filter(lambda item: type(item) == int or type(item) == float, dd))
# print(ints)
#
# y = list(map(lambda sayi: sayi / 2, ints))
# print(y)

# sayilar = list(map(lambda s: s / 2, (filter(lambda item: type(item) == int or type(item) == float, dd))))
#
# print(sayilar)


# list1 = ['A', 'B', 'C']
# list2 = [1, 2, 3]
#
# birlesmis_liste = list(map(lambda x, y: (x + ":" + str(y)), list1, list2))
# print(birlesmis_liste)


dict_1 = {
    1: "A",
    2: "B",
    3: "C",
    4: "D"
}
print(dict_1.items())
# dict_items([(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')])

dict_2 = dict(map(lambda x: (x[0], x[1] + '#' + str(x[0])), dict_1.items()))
print(dict_2)
# {1: 'A#1', 2: 'B#2', 3: 'C#3', 4: 'D#4'}
