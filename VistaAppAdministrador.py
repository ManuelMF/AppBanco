from tkinter import *
import VistaIniSesion
NIF=VistaIniSesion.EntryNIF.get()
VistaIniSesion.raiz.destroy()
raiz=Tk()
raiz.title("Caixa Bank")
raiz.iconbitmap('Recourses/icono.ico')

miFrame=Frame(raiz,width=800, height=600)
miFrame.pack()

lblBienvenida = Label(miFrame, text=NIF)
lblBienvenida.place(x=38,y=50)
lblBienvenida.configure(font=("arial",12,"bold"))

raiz.mainloop()