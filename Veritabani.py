import sqlite3


class Veritabani:

    @staticmethod
    def Kaydet( komut ):
        vt = sqlite3.connect( "PyPara.db" )

        try:
            cursor = vt.cursor( )
            cursor.execute( komut )
            vt.commit( )
            print( "İşlem başarılı" )
        except:
            print( "Kayıt esnasında hata oluştu" )

        vt.close( )

    @staticmethod
    def KurGetir( komut ):
        vt = sqlite3.connect( "PyPara.db" )

        try:
            cursor = vt.cursor( )
            cursor.execute( komut )
            liste_kur = cursor.fetchall( )
            liste_kur.reverse( )
        except:
            print( "Listelemede hata oluştu" )
        return liste_kur
        vt.close( )
