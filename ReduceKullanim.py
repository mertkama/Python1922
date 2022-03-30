##### Reduce() ######

from functools import reduce

numbers = [11, 3, 9, 12, 4, 15, 66]


def findMaxNumber(a, b):
    if a > b:
        return a
    else:
        return b


# for i in range(len(numbers)):
#     if numbers[i] < (len(numbers) + 1):
#         print(findMaxNumber(numbers[i], numbers[i + 1]))


# print(findMaxNumber(66, 99))
# print(reduce(findMaxNumber, numbers))

#
# def faktoryel(s1, s2):
#     return s1 * s2
#
#
# sayilar = range(1, 11)
# print(sayilar)
#
# print(reduce(faktoryel, sayilar))
#
# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# print(reduce(lambda x, y: x * y, liste))
# print(reduce(lambda x, y: x * y, [5, 2, 3, -2, 7]))
#
# print(reduce(lambda x, y: x * y, range(1, 20)))

metinler =  ["Mehmet Nuri Öztürk", "python ve java", "dersini", "anlatıyor"]
print(" ".join(metinler))

def birlestir(metin1, metin2):
    return str(metin1)+ " "+ str(metin2)

print(reduce(birlestir, metinler))