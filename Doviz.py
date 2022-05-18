import datetime
import threading
from tkinter import *
from tkinter.ttk import Notebook

import Grafik
import Kur
from Veritabani import Veritabani


class Doviz:
    pencere = Tk( )

    tab_control = Notebook( pencere )
    tab_altin = Frame( tab_control )
    tab_dolar = Frame( tab_control )
    tab_euro = Frame( tab_control )

    tab_control.add( tab_altin, text="Altın" )
    tab_control.add( tab_dolar, text="Dolar" )
    tab_control.add( tab_euro, text="Euro" )

    tab_control.grid( row=0, column=0, ipadx=10, ipady=10 )

    @classmethod
    def zamanFormat( cls, zamanstr ):
        zamanKisa = [ ]
        for z in zamanstr:
            zmn = datetime.datetime.strptime( z, '%d.%m.%Y %H:%M:%S' )
            zmn = zmn.strftime( '%d.%m %H:%M' )
            zamanKisa.append( zmn )
        return zamanKisa

    @classmethod
    def tekrarla( cls ):

        komut = "SELECT zaman, kur FROM tb_altin ORDER  BY(zaman) DESC"
        altin_kur = Veritabani.KurGetir( komut )
        x = [ row[ 0 ] for row in altin_kur ]
        xf = cls.zamanFormat( x )
        y = [ row[ 1 ] for row in altin_kur ]
        Grafik.Grafik.Ciz( cls.tab_altin, xf, y, "Altın Kuru" )

        komut = "SELECT zaman, kur FROM tb_dolar ORDER  BY(zaman) DESC"
        dolar_kur = Veritabani.KurGetir( komut )
        x = [ row[ 0 ] for row in dolar_kur ]
        xf = cls.zamanFormat( x )
        y = [ row[ 1 ] for row in dolar_kur ]
        Grafik.Grafik.Ciz( cls.tab_dolar, xf, y, "Dolar Kuru" )

        komut = "SELECT zaman, kur FROM tb_euro ORDER  BY(zaman) DESC"
        euro_kur = Veritabani.KurGetir( komut )
        x = [ row[ 0 ] for row in euro_kur ]
        xf = cls.zamanFormat( x )
        y = [ row[ 1 ] for row in euro_kur ]
        Grafik.Grafik.Ciz( cls.tab_euro, xf, y, "Euro Kuru" )

        altin = threading.Thread( target=Kur.Kur.Getir, args=[ "altin" ] )
        dolar = threading.Thread( target=Kur.Kur.Getir, args=[ "dolar" ] )
        euro = threading.Thread( target=Kur.Kur.Getir, args=[ "euro" ] )

        altin.start()
        dolar.start()
        euro.start()

        cls.pencere.after(10000, cls.tekrarla)


altin =  threading.Thread(target=Kur.Kur.Getir, args=["altin"])
dolar =  threading.Thread(target=Kur.Kur.Getir, args=["dolar"])
euro =  threading.Thread(target=Kur.Kur.Getir, args=["euro"])

altin.start()
dolar.start()
euro.start()


Doviz.tekrarla()
Doviz.pencere.mainloop( )
