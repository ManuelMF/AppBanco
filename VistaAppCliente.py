from tkinter import * 
import tkinter as tk
from tkinter import ttk
import Modelo

dni=None

try:
	import VistaIniSesion 
	dni=VistaIniSesion.EntryNIF.get()
	VistaIniSesion.raiz.destroy()
except:
	import VistaCrearCuenta 
	dni=VistaCrearCuenta.EntryDni.get()
	VistaCrearCuenta.raiz.destroy()

#dni="65987412H"

raiz=Tk()
raiz.title("Caixa Bank")
raiz.iconbitmap('Recourses/icono.ico')

miFrame=Frame(raiz,width=490, height=500)
miFrame.pack()


# Barra menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

img_Micuenta = tk.PhotoImage(file="Recourses/Micuenta.png")
img_AdministrarCuentas = tk.PhotoImage(file="Recourses/administrarCuentas.png")

MenuMiCuenta = Menu(barraMenu, tearoff=0)
MenuMiCuenta.add_command(label="Datos personales", image=img_Micuenta, compound=tk.LEFT)
MenuMiCuenta.add_command(label="Administrar cuentas", image=img_AdministrarCuentas, compound=tk.LEFT)
barraMenu.add_cascade(label="Mi cuenta",menu=MenuMiCuenta)

barraMenu.add_command(label="Hacer un ingreso")

barraMenu.add_command(label="Sacar dinero")

barraMenu.add_command(label="Transferencia bancaria")

barraMenu.add_command(label="Cerrar sesion")

lblBienvenida = Label(miFrame, text="Te damos la bienvenida a tu Banca Online")
lblBienvenida.place(x=35,y=30)
lblBienvenida.configure(font=("arial",12,"bold"))

#Combobox
clien= Modelo.cliente.loadCli(None,None,dni)[0]

listacuentas=Modelo.cuenta.loadCue(clien.id,None)
listacuentas2=[]
for i in range(len(listacuentas)):
	nombre=listacuentas[i].nombre
	listacuentas2.append(nombre)

TextMov=Text(miFrame)
scrollVert=Scrollbar(miFrame, command=TextMov.yview,width=14)
scrollVert.place(in_=TextMov, relx=1, relheight=1, bordermode="outside")
TextMov.place(x=35,y=170,width=450,height=200)
TextMov.configure(yscrollcommand=scrollVert.set, padx=10, pady=10)
                  #state='disabled',

def cambiosDeCuenta(self):
	#lo que pasa cuadno se cambia de cuenta
	# cuenta select
	cuentaActual = Modelo.cuenta.loadCue(clien.id,combo.get())[0]
	# saldo de la cuenta
	lblsaldo['text'] = "Saldo actual de la cuenta: "+str(cuentaActual.saldo)
	# lista mov
	listaMovimientos = Modelo.movimiento.loadMov(None,cuentaActual.id)
	TextMov.delete("1.0","end")
	TextMov.insert(INSERT, "Concepto - Saldo anterior - Importe - Saldo - Fecha\n" )
	for i in range(len(listaMovimientos)):
		Mov = listaMovimientos[i]
		
		TextMov.insert(INSERT, Mov.concepto +" - "+ str(Mov.saldoAnterior) +" - "+ str(Mov.saldoActual-Mov.saldoAnterior) +" - "+ str(Mov.saldoActual) +" - "+Mov.fecha + "\n")

combo = ttk.Combobox( state="readonly",
    values=listacuentas2)
combo.place(x=40, y=70)
combo.current(0)
combo.bind("<<ComboboxSelected>>", cambiosDeCuenta)

#cargar Movimientos
cuentaActual = Modelo.cuenta.loadCue(clien.id,combo.get())[0]
listaMovimientos = Modelo.movimiento.loadMov(None,cuentaActual.id)
TextMov.delete("1.0","end")
TextMov.insert(INSERT, "Concepto - Saldo anterior - Importe - Saldo - Fecha\n" )
for i in range(len(listaMovimientos)):
	Mov = listaMovimientos[i]
	TextMov.insert(INSERT, Mov.concepto +" - "+ str(Mov.saldoAnterior) +" - "+ str(Mov.saldoActual-Mov.saldoAnterior) +" - "+ str(Mov.saldoActual) +" - "+Mov.fecha + "\n")	


lblsaldo = Label(miFrame, text="Saldo actual de la cuenta: "+str(Modelo.cuenta.loadCue(clien.id,combo.get())[0].saldo))
lblsaldo.place(x=35,y=100)
lblsaldo.configure(font=("arial",12,"bold"))

lblUltimosMov = Label(miFrame, text="Últimos movimientos")
lblUltimosMov.place(x=35,y=140)
lblUltimosMov.configure(font=("arial",12,"bold"))

--
# hacer mas grande el text y el frame 
# coger el concepto mirar el tamaño que tiene 
# si es mas pequeño contar los espacios que le sobran y meter esos espacios pensar si meter adelante y atras tampoco seria muy dif con un for pimero uno y luego otro o mirar com
# si es mas grande del max quitara 3 y pondrá ...


raiz.mainloop()

