from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.geometry("650x300")


def sonucTemizle():
    entr3.delete(0, END)

def topla():
    s1 = entr1.get()
    s2 = entr2.get()
    sonuc = int(s1) + int(s2)
    sonucTemizle()
    entr3.insert(0, str(sonuc))


def cikar():
    s1 = entr1.get()
    s2 = entr2.get()
    sonuc = int(s1) - int(s2)
    sonucTemizle()
    entr3.insert(0, str(sonuc))


def carp():
    s1 = entr1.get()
    s2 = entr2.get()
    sonuc = int(s1) * int(s2)
    sonucTemizle()
    entr3.insert(0, str(sonuc))


def bol():
    s1 = entr1.get()
    s2 = entr2.get()

    if (int(s2) == 0):
        messagebox.showerror("Hata", "Hiç bir sayı 0'a bölünemez")
    else:
        sonuc = int(s1) / int(s2)
        sonucTemizle()
        entr3.insert(0, float(sonuc))


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

btnTopla = Button(pencere, text="+", width=15, bg="pink", fg="black", font=("Consolas", 12), command=topla)
btnTopla.place(x=450, y=25)

btnCikar = Button(pencere, text="-", width=15, bg="pink", fg="black", font=("Consolas", 12), command=cikar)
btnCikar.place(x=450, y=65)

btnCarp = Button(pencere, text="X", width=15, bg="pink", fg="black", font=("Consolas", 12), command=carp)
btnCarp.place(x=450, y=105)

btnBol = Button(pencere, text="/", width=15, bg="pink", fg="black", font=("Consolas", 12), command=bol)
btnBol.place(x=450, y=150)

mainloop()
