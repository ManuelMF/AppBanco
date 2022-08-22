from tkinter import *
import VistaIniSesion
NIF=VistaIniSesion.EntryNIF.get()
VistaIniSesion.raiz.destroy()
raiz=Tk()

#posicionar ventana
ancho_ventana = 800
alto_ventana = 600
x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

raiz.title("Caixa Bank")
raiz.iconbitmap('Recourses/icono.ico')

miFrame=Frame(raiz,width=800, height=600)
miFrame.pack()

lblBienvenida = Label(miFrame, text=NIF)
lblBienvenida.place(x=38,y=50)
lblBienvenida.configure(font=("arial",12,"bold"))

raiz.mainloop()