from tkinter import *
from tkinter import messagebox
from functools import partial

pencere = Tk()
pencere.geometry("650x300")


def Islem(tip):
    sonuc = ""
    s1 = int(entr1.get())
    s2 = int(entr2.get())

    if tip == "+":
        sonuc = s1 + s2
    elif tip == "-":
        sonuc = s1 - s2
    elif tip == "*":
        sonuc = s1 * s2
    elif tip == "/":
        if (s2 == 0):
            entr1.delete(0, END)
            entr2.delete(0, END)
            entr3.delete(0, END)
            messagebox.showerror("Hata", "Hiç bir sayı 0'a bölünemez")
        else:
            sonuc = s1 / s2

    if sonuc != "":
        entr3.delete(0, END)
        entr3.insert(0, sonuc)

        entr1.delete(0,END)
        entr2.delete(0,END)



lbl1 = Label(pencere, text="1. Sayı", font=("Consolas", 16))
lbl1.place(x=20, y=25)

lbl2 = Label(pencere, text="2. Sayı", font=("Consolas", 16))
lbl2.place(x=20, y=55)

entr1 = Entry(pencere, text="", font=("Consolas", 16))
entr1.place(x=130, y=25)

entr2 = Entry(pencere, text="", font=("Consolas", 16))
entr2.place(x=130, y=55)

lbl_sonuc = Label(pencere, text="SONUÇ", font=("Consolas", 16))
lbl_sonuc.place(x=320, y=190)

entr3 = Entry(pencere, text="", font=("Consolas", 16))
entr3.place(x=250, y=220)


ftopla=partial(Islem,"+")
fCikar=partial(Islem,"-")
fCarp=partial(Islem,"*")
fBol=partial(Islem,"/")

btnTopla = Button(pencere, text="+", width=15, bg="pink", fg="black", font=("Consolas", 12), command=ftopla)
btnTopla.place(x=450, y=25)

btnCikar = Button(pencere, text="-", width=15, bg="pink", fg="black", font=("Consolas", 12), command=fCikar)
btnCikar.place(x=450, y=65)

btnCarp = Button(pencere, text="X", width=15, bg="pink", fg="black", font=("Consolas", 12), command=fCarp)
btnCarp.place(x=450, y=105)

btnBol = Button(pencere, text="/", width=15, bg="pink", fg="black", font=("Consolas", 12), command=fBol)
btnBol.place(x=450, y=150)

mainloop()
