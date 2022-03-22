# sayi = input("Sayi Giriniz: ")  # 1634
#
# #1^4 + 6^4+ 3^4 + 4^4 =  1634
#
# #56236
# #5^5+6^5+2^5+3^5+6^5 = 56236 ise amstrong sayısıdır
#
# if sayi.isdigit():
#     toplam = 0
#     uzunluk = len(sayi)
#     for item in sayi:
#         toplam += int(item) ** uzunluk
#     if toplam == int(sayi):
#         print("Girilen Sayı Amstrong Sayısıdır")
#     else:
#         print("Amstrong sayısı değildir")


for i in range(1000000):
    toplam = 0
    uzunluk = len(str(i))
    for item in str(i):
        toplam += int(item) ** uzunluk

    if toplam == int(i):
        print(i, " bir amstrong sayısıdır")




