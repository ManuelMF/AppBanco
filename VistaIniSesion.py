from tkinter import *
from Controlador import identificarse,abretuCuenta

raiz=Tk()

#posicionar ventana
ancho_ventana = 400
alto_ventana = 350
x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

raiz.title("Caixa Bank  Iniciar sesion")
raiz.iconbitmap('Recourses/icono.ico')

miFrame=Frame(raiz,width=400, height=350)
miFrame.pack()

bg = PhotoImage(file = "Recourses/fondo.png") 
background = Label(miFrame,image = bg).place(x = 0, y = 0, )

lblBienvenida = Label(miFrame, text="Te damos la bienvenida a tu Banca Online")
lblBienvenida.place(x=38,y=50)
lblBienvenida.configure(font=("arial",12,"bold"))

lblNIF = Label(miFrame, text="NIF")
lblNIF.place(x=140,y=90)

lblClave = Label(miFrame, text="Clave de acceso")
lblClave.place(x=140,y=150)

EntryNIF=Entry(miFrame)
EntryNIF.place(x=140,y=110)
EntryNIF.config(justify="center")

EntryPass=Entry(miFrame)
EntryPass.config(show="*")
EntryPass.place(x=140,y=170)
EntryPass.config(justify="center")



buttonIdentificarse=Button(miFrame,text='Identificarse',command=identificarse)
buttonIdentificarse.place(x=160,y=210)

buttonCrearCuenta=Button(miFrame,text='Abre tu cuenta ahora',command=abretuCuenta)
buttonCrearCuenta.place(x=140,y=250)

raiz.mainloop()

