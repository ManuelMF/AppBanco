from tkinter import * 
import tkinter as tk
from tkinter import ttk
import Modelo
import re
from datetime import datetime

dni=None

try:
	import VistaIniSesion 
	dni=VistaIniSesion.EntryNIF.get()
	VistaIniSesion.raiz.destroy()
except:
	import VistaCrearCuenta 
	dni=VistaCrearCuenta.EntryDni.get()
	VistaCrearCuenta.raiz.destroy()

raiz=Tk()
raiz.title("Caixa Bank")
raiz.iconbitmap('Recourses/icono.ico')
raiz.resizable(0,0)

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

class VentanaHacerIngreso():
	def __init__(self):
		self.raizI=Tk()
		self.raizI.title("Ingreso")
		self.raizI.resizable(0,0)
		self.raizI.iconbitmap('Recourses/icono.ico')

		self.miFrameI=Frame(self.raizI,width=350, height=180)
		self.miFrameI.configure(bg='cornsilk')
		self.miFrameI.pack()

		self.lblCuenta = Label(self.miFrameI, text=Modelo.cuenta.loadCue(clien.id,combo.get())[0].nombre)
		self.lblCuenta.place(x=35,y=30)
		self.lblCuenta.configure(font=("arial",9,"bold"))
		self.lblCuenta.configure(bg='cornsilk')

		self.lblIngreso = Label(self.miFrameI, text="Dinero a ingresar:")
		self.lblIngreso.place(x=190,y=60)
		self.lblIngreso.configure(font=("arial",8,"bold"))
		self.lblIngreso.configure(bg='cornsilk')
		self.EntryIng=Entry(self.miFrameI)
		self.EntryIng.place(x=190,y=85)

		self.lblconcepto = Label(self.miFrameI, text="Concepto:")
		self.lblconcepto.place(x=35,y=60)
		self.lblconcepto.configure(font=("arial",8,"bold"))
		self.lblconcepto.configure(bg='cornsilk')
		self.EntryConcepto=Entry(self.miFrameI)
		self.EntryConcepto.place(x=35,y=85)

		self.btnIngreso = Button(self.raizI,text="Ingresar", command=lambda: self.Ingreso())
		self.btnIngreso.place(x=107,y=120)

		self.btnCancelar = Button(self.raizI,text="Cancelar", command=lambda: self.Cancelar())
		self.btnCancelar.place(x=190,y=120)

		self.raizI.mainloop()
	
	def Ingreso(self):
		cue = Modelo.cuenta.loadCue(clien.id,combo.get())[0]
		ingreso = self.EntryIng.get()
		try:
			if ingreso>0:
				Modelo.movimiento.crearMov(self.EntryConcepto.get(),cue.saldo,cue.saldo+int(ingreso),cue.id,datetime.now().strftime('%Y-%m-%d'))
				self.raizI.destroy()
				cambiosDeCuenta()
		except:
			pass

	def Cancelar(self):
		self.raizI.destroy()

class VentanaHacerRetirada():
	def __init__(self):
		self.raizR=Tk()
		self.raizR.title("Retirar ingresos")
		self.raizR.resizable(0,0)


		self.miFrameR=Frame(self.raizR,width=350, height=180)
		self.miFrameR.configure(bg='cornsilk')
		self.miFrameR.pack()

		self.lblCuenta = Label(self.miFrameR, text=Modelo.cuenta.loadCue(clien.id,combo.get())[0].nombre)
		self.lblCuenta.place(x=35,y=30)
		self.lblCuenta.configure(font=("arial",9,"bold"))
		self.lblCuenta.configure(bg='cornsilk')

		self.lblRetirada = Label(self.miFrameR, text="Dinero a Retirar:")
		self.lblRetirada.place(x=190,y=60)
		self.lblRetirada.configure(font=("arial",8,"bold"))
		self.lblRetirada.configure(bg='cornsilk')
		self.EntryRe=Entry(self.miFrameR)
		self.EntryRe.place(x=190,y=85)
		
		self.lblconcepto = Label(self.miFrameR, text="Concepto:")
		self.lblconcepto.place(x=35,y=60)
		self.lblconcepto.configure(font=("arial",8,"bold"))
		self.lblconcepto.configure(bg='cornsilk')
		self.EntryConcepto=Entry(self.miFrameR)
		self.EntryConcepto.place(x=35,y=85)

		self.btnIngreso = Button(self.raizR,text="Retirar", command=lambda: self.Retirada())
		self.btnIngreso.place(x=115,y=120)

		self.btnCancelar = Button(self.raizR,text="Cancelar", command=lambda: self.Cancelar())
		self.btnCancelar.place(x=190,y=120)

		self.raizR.mainloop()
	
	def Retirada(self):
		cue = Modelo.cuenta.loadCue(clien.id,combo.get())[0]
		retirada = int(self.EntryRe.get())* -1
		try:
			if retirada<0:
				Modelo.movimiento.crearMov(self.EntryConcepto.get(),cue.saldo,cue.saldo+int(retirada),cue.id,datetime.now().strftime('%Y-%m-%d'))
				self.raizR.destroy()
				cambiosDeCuenta()
		except:
			pass

	def Cancelar(self):
		self.raizR.destroy()

barraMenu.add_command(label="Hacer un ingreso", command=VentanaHacerIngreso)

barraMenu.add_command(label="Sacar dinero", command=VentanaHacerRetirada)

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

def cambiosDeCuenta():
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
def atajo(self):
	cambiosDeCuenta()
combo.bind("<<ComboboxSelected>>", atajo)


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
cuentaActual = Modelo.cuenta.loadCue(clien.id,combo.get())[0]
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

cambiosDeCuenta()

raiz.mainloop()


		