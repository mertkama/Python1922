rakamlar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# for i in rakamlar:
#     print(i)

# basamak = iter(rakamlar)
# print(next(basamak)) # ilk eleman basamak[0]
# print(next(basamak)) # ikinci eleman
# print(next(basamak))
# print(next(basamak))
#
# basamak = iter(rakamlar) #başadöner


def onunKatlari():
    yield 10  # genetator oluşturmanın kısa yolu
    yield 20
    yield 30


test = onunKatlari()
print(next(test))
print(next(test))
print(next(test))


def ozel_generatorum():
    i = 1
    print("Birinci")
    yield i

    i += 1
    print("İkinci")
    yield i

    i += 1
    print("Ucuncu")
    yield i

a = ozel_generatorum()
print(next(a))
print(next(a))
print(next(a))


def tek_tek_yazdir(kelime):
    'Dongu Yield'
    length = len(kelime)
    for i in range(length -1,-1,-1):
        yield kelime[i]

for char in tek_tek_yazdir("Merhaba Dünya"):
    print(char)


listem = [1,3,6,10]

print( [x**2 for x in listem] )

a =  (x**2 for x in listem)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(sum( (x**2 for x in listem)))
print(max( (x**2 for x in listem)))
print(min( (x**2 for x in listem)))

