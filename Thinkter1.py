# TKİNTER, GTK, PyQT, PySide(Like Pyqt) GUI

from tkinter import *

pencere = Tk()
pencere.title("Merhaba")

#
def clicked():
    print("Merhaba, bana tıkladı")


button1 = Button()
button1.config(text="Bana Tıkla", bg="yellow", fg="red", command=clicked)
button1.pack()


entry1 = Entry()
entry1.pack()

etiket = Label()
etiket.config(text="Merhaba TK" , bg="red", fg="orange", font=("Vertana", 24))
etiket.pack()

mainloop()
