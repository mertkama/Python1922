import datetime
def Kontrol(sayi):
    dd = open("log.txt", "a", encoding="utf-8")
    while True:
        try:
            sayi = int(sayi)
            print(sayi * 2)
            print(sayi / 0)
        except Exception as e:

            print("{} -> {} Hatası".format(datetime.datetime.now().strftime("%Y.%m.%d %H:%M"), e.__class__.__name__),
                  file=dd)
            break