# TKİNTER, GTK, PyQT, PySide(Like Pyqt) GUI

from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("PLACE KULLANIMI")
pencere.geometry("500x500")  # .geometry(Width,Height+Ekran konumu(x+y))

def temizle():
    degistirilecek_yazi.delete(0, END)

def degistir():
    temizle()
    degistirilecek_yazi.insert(0, metin.get())
    metin.delete(0,END)

def tip_goster():
    # messagebox.showerror("Hata","Hata mesajı")
    messagebox.showinfo("Bilgi", type(degistirilecek_yazi.get()))
    # messagebox.showwarning("Warning", "Warning")
    # messagebox.askyesno("ss","ss",icon = 'warning')

label = Label(pencere, text="Değiştir", bg="orange", fg="blue", font=("Verdana", 14))
label.place(x=5, y=5)

btn_temizle = Button(pencere, text="Temizle", bg="blue", fg="white", font=("Verdana", 14), command=temizle)
btn_temizle.place(x=220, y=10)

label2 = Label(pencere, text="Değiştirilecek Yazı", bg="orange", fg="blue", font=("Verdana", 14))
label2.place(x=5, y=80)

btn_degistir = Button(pencere, text="Değiştir", bg="blue", fg="white", font=("Verdana", 14), command=degistir)
btn_degistir.place(x=220, y=80)

degistirilecek_yazi = Entry(pencere, text="", font=("Verdana", 10), width=20)
degistirilecek_yazi.place(x=5, y=40, )

metin = Entry(pencere, text="", font=("Verdana", 10), width=20)
metin.place(x=5, y=120)

tipgosterbtn =  Button(pencere, text="Tip Goster", command=tip_goster,bg="red", fg="white", font=("Verdana", 14))
tipgosterbtn.place(x=220, y=180)

mainloop()
