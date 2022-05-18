from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

pencere = Tk( )
pencere.geometry( "640x480+250+100" )
pencere.config( bg="orange" )
pencere.title( "TEST" )
pencere.minsize( 640, 840 )
pencere.maxsize( 800, 600 )
pencere.resizable( False, True )

kurs_icon = PhotoImage( file="icon.png" )
pencere.iconphoto( False, kurs_icon )

lbl_ad = Label( pencere, text="AD", bg="pink", fg="black", font=("Consolas", 16) )
text_ad = Entry( pencere, font=("Consolas", 16) )

lbl_soyad = Label( pencere, text="SOYAD", bg="pink", fg="black", font=("Consolas", 16) )
text_soyad = Entry( pencere, font=("Consolas", 16) )

img = PhotoImage( file="kus.gif" )
img = img.subsample( 10, 10 )
lbl_img = Label( pencere, image=img )

onay_kutusu_degisken = StringVar( )
onay_kutusu = Checkbutton( pencere, text="Hatırlansın Mı?", variable=onay_kutusu_degisken, onvalue="EVET",
                           offvalue="HAYIR", font=("Consolas", 16)
                           )


def Sonuc():
    lbl_sonuc_ad["text"] = str(text_ad.get())
    lbl_sonuc_soyad["text"] = str(text_soyad.get())
    lbl_sonuc_control["text"] =  "Hatırla Kutusun İşaretli Mi ?" + str(onay_kutusu_degisken.get())
    lbl_cbx["text"] = str(cbx.get())

    secilenler =  lbx.curselection()
    lbl_sonuc_lbl["text"] = ""
    for i in secilenler:
        lbl_sonuc_lbl["text"] += str(lbx.get(i)) + "\n"

    lbl_radio["text"] = str(erkek_degisken.get())





btn_kontrol = Button( pencere, text="Kontrol ET", font=("Consolas", 16), bg="blue", fg="white", command=Sonuc )

# Konumlanırma
# ROW = SATIR , COLUMN = SÜTUN EXCELL MANTIĞI
lbl_ad.grid( row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5 )
text_ad.grid( row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5 )

lbl_soyad.grid( row=1, column=0, padx=5, pady=5, ipadx=5, ipady=5 )
text_soyad.grid( row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5 )

lbl_img.grid( row=0, column=2, rowspan=2, padx=5, pady=5, ipadx=5, ipady=5 )
onay_kutusu.grid( row=2, column=0, columnspan=2 )

btn_kontrol.grid( row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5 )

# ALT SONUÇ BöLÜMLERi
cerceve_sonu = Label( pencere, bg="lavender", text="", height=4, width=10 )
cerceve_sonu.grid( row=4, column=1, columnspan=4 )

lbl_sonuc_ad = Label( cerceve_sonu, bg="yellow", text="22", font=("Consolas", 16) )
lbl_sonuc_ad.grid( row=0, column=0, columnspan=4 )

lbl_sonuc_soyad = Label( cerceve_sonu, bg="yellow", text="asd", font=("Consolas", 16) )
lbl_sonuc_soyad.grid( row=1, column=0, columnspan=4 )

lbl_sonuc_control = Label( cerceve_sonu, bg="red", text="ssa", font=("Consolas", 16) )
lbl_sonuc_control.grid( row=2, column=0, columnspan=4 )

lbl_cbx = Label( cerceve_sonu, text="aa", font=("Consolas", 16) )
lbl_cbx.grid( row=3, column=0, columnspan=4 )

lbl_sonuc_lbl =  Label(cerceve_sonu, text="skk", font=("Consolas", 16))
lbl_sonuc_lbl.grid(row=4, column=0, columnspan=4)


lbl_radio = Label(cerceve_sonu, text="sdada",  font=("Consolas", 16))
lbl_radio.grid(row=5, column=0, columnspan=4)


liste = ["İSTANBUL", "ANKARA", "İZMİR", "BURSA", "ADANA", "KAYSERİ", "SİVAS", "MALATYA"]
cbx = Combobox(pencere,values=liste)
cbx.current(7)
cbx.grid(row=3, column=0)


liste2 = ["MERSİN", "KIRKLARELİ", "SAMSUN", "TRABZON","TRAKYA", "MANİSA"]

lbx =  Listbox(pencere, height=len(liste2), selectmode="multiple")

for elaman in liste2:
    lbx.insert(END,elaman)

lbx.grid(row=3, column=1)


erkek_degisken = StringVar()
kadin_degisken = StringVar()

rdbe =  Radiobutton(pencere, text="Erkek", value="erkek", variable=erkek_degisken)
rdbk =  Radiobutton(pencere, text="Kadın", value="kadin", variable=kadin_degisken)

rdbe.grid(row=3, column=2)
rdbk.grid(row=3, column=3)


mainloop( )
