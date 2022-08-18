from tkinter import *
from Controlador import CrearCuenta

raiz=Tk()
raiz.title("Caixa Bank  Crear cuenta")
raiz.iconbitmap('Recourses/icono.ico')

miFrame=Frame(raiz,width=400, height=530)
miFrame.pack()

lblBienvenida = Label(miFrame, text="Crea tu cuenta online aqui")
lblBienvenida.place(x=100,y=50)
lblBienvenida.configure(font=("arial",12,"bold"))

lblNombre = Label(miFrame, text="Nombre")
lblNombre.place(x=140,y=90)

lblApellidos = Label(miFrame, text="Apellidos")
lblApellidos.place(x=140,y=150)

lblFechaNacimiento = Label(miFrame, text="FechaNacimiento")
lblFechaNacimiento.place(x=140,y=210)

lblDni = Label(miFrame, text="Dni")
lblDni.place(x=140,y=270)

lblTelefono = Label(miFrame, text="Telefono")
lblTelefono.place(x=140,y=330)

lblClave = Label(miFrame, text="Clave de acceso")
lblClave.place(x=140,y=390)


EntryNombre = Entry(miFrame)
EntryNombre.place(x=140,y=110)

EntryApellidos = Entry(miFrame)
EntryApellidos.place(x=140,y=170)

EntryFechaNacimientoD = Entry(miFrame)
EntryFechaNacimientoD.place(x=140,y=230,width=30)
EntryFechaNacimientoD.config(justify="center")

EntryFechaNacimientoM = Entry(miFrame)
EntryFechaNacimientoM.place(x=180,y=230,width=30)
EntryFechaNacimientoM.config(justify="center")

EntryFechaNacimientoA = Entry(miFrame)
EntryFechaNacimientoA.place(x=220,y=230,width=45)
EntryFechaNacimientoA.config(justify="center")

EntryDni = Entry(miFrame)
EntryDni.place(x=140,y=290)

EntryTelefono = Entry(miFrame)
EntryTelefono.place(x=140,y=350)

EntryClave = Entry(miFrame)
EntryClave.config(show="*")
EntryClave.place(x=140,y=410)

buttonCrearCuenta=Button(miFrame,text='Crear cuenta',command=CrearCuenta)
buttonCrearCuenta.place(x=160,y=450)

raiz.mainloop()

