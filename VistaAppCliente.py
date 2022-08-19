from tkinter import * 
import tkinter as tk
from tkinter import ttk
import Modelo
import re

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

miFrame=Frame(raiz,width=550, height=500)
miFrame.configure(bg='cornsilk')
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
lblBienvenida.configure(bg='cornsilk')

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
TextMov.place(x=35,y=170,width=480,height=200)
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
	TextMov.insert(INSERT, "  Concepto   - Saldo ant - Importe - Saldo  - Fecha\n" )
	for i in range(len(listaMovimientos)):
		Mov = listaMovimientos[i]

		#meter espacios 
		if len(Mov.concepto)>13:
			Mov.concepto=Mov.concepto[:10]+"..."
		elif(len(Mov.concepto)<13):
			for i in range(13-len(Mov.concepto)):
				Mov.concepto = Mov.concepto+" "

		importe=Mov.saldoActual-Mov.saldoAnterior

		if len(str(Mov.saldoAnterior))<10:
			for i in range(10-len(str(Mov.saldoAnterior))):
				if i % 2 == 0:
					Mov.saldoAnterior = str(Mov.saldoAnterior)+" "
				else:
					Mov.saldoAnterior = " "+str(Mov.saldoAnterior)

		if len(str(importe))<8:
			for i in range(8-len(str(importe))):
				if i % 2 == 0:
					importe = str(importe)+" "
				else:
					importe = " "+str(importe)

		if len(str(Mov.saldoActual))<7:
			for i in range(7-len(str(Mov.saldoActual))):
				if i % 2 == 0:
					Mov.saldoActual = str(Mov.saldoActual)+" "
				else:
					Mov.saldoActual = " "+str(Mov.saldoActual)

		TextMov.insert(INSERT, Mov.concepto +"- "+ Mov.saldoAnterior +"- "+ str(importe) +"- "+ str(Mov.saldoActual) +"- "+Mov.fecha + "\n")
	
	ingresos=0
	gastos=0
	listaMovimientos = Modelo.movimiento.loadMov(None,cuentaActual.id)
	for i in range(len(listaMovimientos)):
		Mov = listaMovimientos[i]
		importe=Mov.saldoActual-Mov.saldoAnterior
		if importe>0:
			ingresos+=importe
		else:
			gastos+=importe
	lblIngresosNum.configure(text="+"+str(ingresos)) 
	lblGastosNum.configure(text=str(gastos))

combo = ttk.Combobox( state="readonly",
    values=listacuentas2)
combo.place(x=40, y=70)
combo.current(0)
combo.bind("<<ComboboxSelected>>", cambiosDeCuenta)

#cargar Movimientos
cuentaActual = Modelo.cuenta.loadCue(clien.id,combo.get())[0]
listaMovimientos = Modelo.movimiento.loadMov(None,cuentaActual.id)
TextMov.delete("1.0","end")
TextMov.insert(INSERT, "  Concepto   - Saldo ant - Importe - Saldo  - Fecha\n" )
for i in range(len(listaMovimientos)):
		Mov = listaMovimientos[i]

		#meter espacios 
		if len(Mov.concepto)>13:
			Mov.concepto=Mov.concepto[:10]+"..."
		elif(len(Mov.concepto)<13):
			for i in range(13-len(Mov.concepto)):
				Mov.concepto = Mov.concepto+" "

		importe=Mov.saldoActual-Mov.saldoAnterior

		if len(str(Mov.saldoAnterior))<10:
			for i in range(10-len(str(Mov.saldoAnterior))):
				if i % 2 == 0:
					Mov.saldoAnterior = str(Mov.saldoAnterior)+" "
				else:
					Mov.saldoAnterior = " "+str(Mov.saldoAnterior)

		if len(str(importe))<8:
			for i in range(8-len(str(importe))):
				if i % 2 == 0:
					importe = str(importe)+" "
				else:
					importe = " "+str(importe)

		if len(str(Mov.saldoActual))<7:
			for i in range(7-len(str(Mov.saldoActual))):
				if i % 2 == 0:
					Mov.saldoActual = str(Mov.saldoActual)+" "
				else:
					Mov.saldoActual = " "+str(Mov.saldoActual)

		TextMov.insert(INSERT, Mov.concepto +"- "+ Mov.saldoAnterior +"- "+ str(importe) +"- "+ str(Mov.saldoActual) +"- "+Mov.fecha + "\n")

lblsaldo = Label(miFrame, text="Saldo actual de la cuenta: "+str(Modelo.cuenta.loadCue(clien.id,combo.get())[0].saldo))
lblsaldo.place(x=35,y=100)
lblsaldo.configure(font=("arial",12,"bold"))
lblsaldo.configure(bg='cornsilk')

lblUltimosMov = Label(miFrame, text="Últimos movimientos")
lblUltimosMov.place(x=35,y=140)
lblUltimosMov.configure(font=("arial",12,"bold"))
lblUltimosMov.configure(bg='cornsilk')

ingresos=0
gastos=0
listaMovimientos = Modelo.movimiento.loadMov(None,cuentaActual.id)

for i in range(len(listaMovimientos)):
		Mov = listaMovimientos[i]
		importe=Mov.saldoActual-Mov.saldoAnterior
		if importe>0:
			ingresos+=importe
		else:
			gastos+=importe

lblIngresos = Label(miFrame, text="Ingresos")
lblIngresos.place(x=50,y=400)
lblIngresos.configure(bg='cornsilk', font="bold")
lblIngresosNum = Label(miFrame, text="+"+str(ingresos))
lblIngresosNum.place(x=50,y=430)
lblIngresosNum.configure(bg='cornsilk', fg='lime', font="bold")

lblGastos = Label(miFrame, text="Gastos")
lblGastos.place(x=130,y=400)
lblGastos.configure(bg='cornsilk', font="bold")
lblGastosNum = Label(miFrame, text=str(gastos))
lblGastosNum.place(x=130,y=430)
lblGastosNum.configure(bg='cornsilk', fg='red', font="bold")

raiz.mainloop()

