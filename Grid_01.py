from tkinter import *
from tkinter import messagebox
from time import *

pencere = Tk( )
pencere.geometry( "500x250" )
pencere.maxsize( 1024, 768 )
pencere.config( bg="lightgray" )
kurs_ikon = PhotoImage( file="icon.png" )
pencere.iconphoto( True, kurs_ikon )


def dialog( ):
    var = messagebox.showinfo( "Bilgi", "Python Programlama" )
    print( var )
    sleep( 2 )
    yok = messagebox.askyesnocancel( "Hata", "Uyarı Aldınız !" )
    if yok == True:
        return dialog( )


uygulama = Frame( pencere )
uygulama.grid( )

button1 = Button( uygulama, text="Mesaj Ver", width=20, command=dialog )
button1.grid( padx=110, pady=80 )

mainloop( )
