# list1 = ["Ahmet", "Mehmet", "ALi", "Ayşe"]
# list2 = [33, 44, 66, 44]
# print(list(zip(list1, list2)))

# isim        = ["Mehmet Nuri", "Fatma", "Kadriye", "Umur", "Hatice", "Duygu"]
# kullaniciAd = ["mnozturk", "fakdeniz", "kaslan", "uguneysu", "hkalkan", "dbarlas"]
#
# uyelerim = list(zip(isim,kullaniciAd))
#
# for i,u in uyelerim:
#     print("{} ->  {} ".format(i,u))


isim = ["Mehmet Nuri", "Fatma", "Kadriye", "Umur", "Hatice", "Duygu"]

tarihler = [1993, 1996, 1997, 2001, 1999, 2000]

print(list(
    filter(
        lambda x: 1996 <= x[1] <= 2000, zip(isim, tarihler)
    )
))
