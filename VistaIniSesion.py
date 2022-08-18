from tkinter import *
from Controlador import identificarse,abretuCuenta
raiz=Tk()
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

EntryPass=Entry(miFrame)
EntryPass.config(show="*")
EntryPass.place(x=140,y=170)

buttonIdentificarse=Button(miFrame,text='Identificarse',command=identificarse)
buttonIdentificarse.place(x=160,y=210)

buttonCrearCuenta=Button(miFrame,text='Abre tu cuenta ahora',command=abretuCuenta)
buttonCrearCuenta.place(x=140,y=250)



raiz.mainloop()

