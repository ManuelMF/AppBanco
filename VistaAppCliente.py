from tkinter import * 
import tkinter as tk
from tkinter import ttk
import Modelo
import re
from datetime import datetime
from tkinter import messagebox

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

#posicionar ventana
ancho_ventana = 550
alto_ventana = 500
x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

raiz.title("Caixa Bank")
raiz.iconbitmap('Recourses/icono.ico')
raiz.resizable(0,0)

miFrame=Frame(raiz,width=550, height=500)
miFrame.configure(bg='cornsilk')
miFrame.pack()

		
class VentanaDatosPersonales():
	def __init__(self):

		self.raizD=Tk()
		self.raizD.title("Datos ")
		self.raizD.resizable(0,0)
		self.raizD.iconbitmap('Recourses/icono.ico')

		#posicionar ventana
		ancho_ventana = 250
		alto_ventana = 310
		x_ventana = self.raizD.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = self.raizD.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		self.raizD.geometry(posicion)

		self.miFrameI=Frame(self.raizD,width=250, height=310)
		self.miFrameI.configure(bg='cornsilk')
		self.miFrameI.pack()

		cli = Modelo.cliente.loadCli(None,None,dni)[0]

		self.lblnombre= Label(self.miFrameI, text="Nombre:")
		self.lblnombre.place(x=70,y=30)
		self.lblnombre.configure(font=("arial",9,"bold"),bg='cornsilk')
			
		self.lblnombreR= Label(self.miFrameI, text=cli.nombre)
		self.lblnombreR.place(x=70,y=50)
		self.lblnombreR.configure(font=("arial",9),bg='cornsilk')

		self.lblapellidos= Label(self.miFrameI, text="Apellidos:")
		self.lblapellidos.place(x=70,y=80)
		self.lblapellidos.configure(font=("arial",9,"bold"),bg='cornsilk')

		self.lblapellidosR= Label(self.miFrameI, text=cli.apellidos)
		self.lblapellidosR.place(x=70,y=100)
		self.lblapellidosR.configure(font=("arial",9),bg='cornsilk')

		self.lblDni= Label(self.miFrameI, text="Dni:")
		self.lblDni.place(x=70,y=130)
		self.lblDni.configure(font=("arial",9,"bold"),bg='cornsilk')

		self.lblDniR= Label(self.miFrameI, text=cli.dni)
		self.lblDniR.place(x=70,y=150)
		self.lblDniR.configure(font=("arial",9),bg='cornsilk')

		self.lblfechaNacimiento= Label(self.miFrameI, text="Fecha de nacimiento:")
		self.lblfechaNacimiento.place(x=70,y=180)
		self.lblfechaNacimiento.configure(font=("arial",9,"bold"),bg='cornsilk')

		anyo = cli.fechaNacimiento[:4]
		mes = cli.fechaNacimiento[5:7]
		dia = cli.fechaNacimiento[8:10]
		fecha = dia+"/"+mes+"/"+anyo

		self.lblfechaNacimientoR= Label(self.miFrameI, text=fecha)
		self.lblfechaNacimientoR.place(x=70,y=200)
		self.lblfechaNacimientoR.configure(font=("arial",9),bg='cornsilk')

		self.lbltelefono= Label(self.miFrameI, text="Teléfono:")
		self.lbltelefono.place(x=70,y=230)
		self.lbltelefono.configure(font=("arial",9,"bold"),bg='cornsilk')

		self.lbltelefonoR= Label(self.miFrameI, text=cli.telefono)
		self.lbltelefonoR.place(x=70,y=250)
		self.lbltelefonoR.configure(font=("arial",9),bg='cornsilk')

		self.raizD.mainloop()

class AdministrarCuentas():
	def __init__(self):

		self.raizD=Tk()
		self.raizD.title("Cuentas")
		self.raizD.resizable(0,0)
		self.raizD.iconbitmap('Recourses/icono.ico')

		#posicionar ventana
		ancho_ventana = 250
		alto_ventana = 310
		x_ventana = self.raizD.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = self.raizD.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		self.raizD.geometry(posicion)

		self.miFrameI=Frame(self.raizD,width=250, height=310)
		self.miFrameI.configure(bg='cornsilk')
		self.miFrameI.pack()

		cli = Modelo.cliente.loadCli(None,None,dni)[0]

		self.lblclinombre= Label(self.miFrameI, text=cli.nombre+" "+cli.apellidos)
		self.lblclinombre.place(x=50,y=25)
		self.lblclinombre.configure(font=("arial",9,"bold"),bg='cornsilk')

		self.lblcuentas= Label(self.miFrameI, text="Cuentas:")
		self.lblcuentas.place(x=50,y=55)
		self.lblcuentas.configure(font=("arial",9,"bold"),bg='cornsilk')
			
		listacuentas=Modelo.cuenta.loadCue(cli.id,None,None)
		listacuentas2=[]
		for i in range(len(listacuentas)):
			nombre=listacuentas[i].nombre
			listacuentas2.append(nombre)

		self.combob = ttk.Combobox(self.miFrameI, state="readonly",
   		values=listacuentas2)
		self.combob.place(x=50, y=75)
		self.combob.current(0)
		
		self.btnEliminarCue=Button(self.miFrameI,text="Eliminar Cuenta", command=lambda: self.eliminarCue())
		self.btnEliminarCue.place(x=75,y=110) 

		self.lblCrearCue= Label(self.miFrameI, text="Crear cuenta:")
		self.lblCrearCue.place(x=50,y=150)
		self.lblCrearCue.configure(font=("arial",9,"bold"),bg='cornsilk')

		self.lblConcepto= Label(self.miFrameI, text="Concepto:")
		self.lblConcepto.place(x=50,y=170)
		self.lblConcepto.configure(font=("arial",9),bg='cornsilk')

		self.EntryCrearCue=Entry(self.miFrameI)
		self.EntryCrearCue.place(x=50,y=190)

		self.btnCrearCue=Button(self.miFrameI,text="Crear cuenta", command=lambda: self.CrearCue())
		self.btnCrearCue.place(x=80,y=225) 

		self.raizD.mainloop()

	def eliminarCue(self):
		cli = Modelo.cliente.loadCli(None,None,dni)[0]
		cue = Modelo.cuenta.loadCue(cli.id,self.combob.get(),None)[0]

		if cue.saldo > 0:
			messagebox.showwarning("Error borrando cuenta", cue.nombre+" aun tiene dinero, "+str(cue.saldo)+"€")
		elif cue.saldo < 0: 
			messagebox.showwarning("Error borrando cuenta", cue.nombre+" aun tiene deudas, "+str(cue.saldo)+"€")
		else:
			cue.borrarCuenta()
			self.raizD.destroy()

			listacuentas=Modelo.cuenta.loadCue(clien.id,None,None)
			listacuentas2=[]
			for i in range(len(listacuentas)):
				nombre=listacuentas[i].nombre
				listacuentas2.append(nombre)
			combo['values'] = listacuentas2
			combo.current(0)
			cambiosDeCuenta()

	def CrearCue(self):
		cli = Modelo.cliente.loadCli(None,None,dni)[0]
		#try:
		Modelo.cuenta.crearCuenta(self.EntryCrearCue.get(),0,datetime.now().strftime('%Y-%m-%d'),cli.id)
		self.raizD.destroy()

		listacuentas=Modelo.cuenta.loadCue(clien.id,None,None)
		listacuentas2=[]
		for i in range(len(listacuentas)):
			nombre=listacuentas[i].nombre
			listacuentas2.append(nombre)
		combo['values'] = listacuentas2
		combo.current(len(listacuentas2)-1)
		cambiosDeCuenta()
		#except:
		#	messagebox.showwarning("Error","Error creando cuenta")

class VentanaHacerIngreso():
	def __init__(self):
		self.raizI=Tk()
		self.raizI.title("Ingreso")
		self.raizI.resizable(0,0)
		self.raizI.iconbitmap('Recourses/icono.ico')

		#posicionar ventana
		ancho_ventana = 350
		alto_ventana = 180
		x_ventana = self.raizI.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = self.raizI.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		self.raizI.geometry(posicion)

		self.miFrameI=Frame(self.raizI,width=350, height=180)
		self.miFrameI.configure(bg='cornsilk')
		self.miFrameI.pack()

		self.lblCuenta = Label(self.miFrameI, text=Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0].nombre)
		self.lblCuenta.place(x=35,y=30)
		self.lblCuenta.configure(font=("arial",9,"bold"),bg='cornsilk')
		

		self.lblIngreso = Label(self.miFrameI, text="Dinero a ingresar:")
		self.lblIngreso.place(x=190,y=60)
		self.lblIngreso.configure(font=("arial",8,"bold"),bg='cornsilk')
		self.EntryIng=Entry(self.miFrameI)
		self.EntryIng.place(x=190,y=85)

		self.lblconcepto = Label(self.miFrameI, text="Concepto:")
		self.lblconcepto.place(x=35,y=60)
		self.lblconcepto.configure(font=("arial",8,"bold"),bg='cornsilk')
		self.EntryConcepto=Entry(self.miFrameI)
		self.EntryConcepto.place(x=35,y=85)

		self.btnIngreso = Button(self.raizI,text="Ingresar", command=lambda: self.Ingreso())
		self.btnIngreso.place(x=107,y=120)

		self.btnCancelar = Button(self.raizI,text="Cancelar", command=lambda: self.Cancelar())
		self.btnCancelar.place(x=190,y=120)

		self.raizI.mainloop()
	
	def Ingreso(self):
		cue = Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0]
		ingreso = self.EntryIng.get()

		try:
			if int(ingreso)>0:
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

		#posicionar ventana
		ancho_ventana = 350
		alto_ventana = 180
		x_ventana = self.raizR.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = self.raizR.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		self.raizR.geometry(posicion)

		self.miFrameR=Frame(self.raizR,width=350, height=180)
		self.miFrameR.configure(bg='cornsilk')
		self.miFrameR.pack()

		self.lblCuenta = Label(self.miFrameR, text=Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0].nombre)
		self.lblCuenta.place(x=35,y=30)
		self.lblCuenta.configure(font=("arial",9,"bold"),bg='cornsilk')

		self.lblRetirada = Label(self.miFrameR, text="Dinero a Retirar:")
		self.lblRetirada.place(x=190,y=60)
		self.lblRetirada.configure(font=("arial",8,"bold"),bg='cornsilk')
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
		cue = Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0]
		retirada = int(self.EntryRe.get())* -1
		try:
			if retirada<0 and 200+cue.saldo>= retirada* -1:
				Modelo.movimiento.crearMov(self.EntryConcepto.get(),cue.saldo,cue.saldo+int(retirada),cue.id,datetime.now().strftime('%Y-%m-%d'))
				self.raizR.destroy()
				cambiosDeCuenta()
			else:
				messagebox.showwarning("Error", "Saldo insuficiente")
		except:
			pass

	def Cancelar(self):
		self.raizR.destroy()

class VentanaHacerTransferencia():
	def __init__(self):
		self.raizR=Tk()
		self.raizR.title("Transferencia")
		self.raizR.resizable(0,0)

		#posicionar ventana
		ancho_ventana = 250
		alto_ventana = 280
		x_ventana = self.raizR.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = self.raizR.winfo_screenheight() // 2 - alto_ventana // 2
		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		self.raizR.geometry(posicion)

		self.miFrameR=Frame(self.raizR,width=250, height=280)
		self.miFrameR.configure(bg='cornsilk')
		self.miFrameR.pack()

		self.lblCuenta = Label(self.miFrameR, text=Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0].nombre)
		self.lblCuenta.place(x=60,y=30)
		self.lblCuenta.configure(font=("arial",9,"bold"),bg='cornsilk')

		self.lblNumCuenta = Label(self.miFrameR, text="Número de cuenta:")
		self.lblNumCuenta.place(x=60,y=60)
		self.lblNumCuenta.configure(font=("arial",8,"bold"),bg='cornsilk')
		self.EntryNumCue=Entry(self.miFrameR)
		self.EntryNumCue.place(x=60,y=85)
		self.EntryNumCue.config(justify="center")

		self.lblImporte = Label(self.miFrameR, text="Importe:")
		self.lblImporte.place(x=60,y=165)
		self.lblImporte.configure(font=("arial",8,"bold"),bg='cornsilk')
		self.EntryImport=Entry(self.miFrameR)
		self.EntryImport.place(x=60,y=185)
		self.EntryImport.config(justify="center")

		self.lblconcepto = Label(self.miFrameR, text="Concepto:")
		self.lblconcepto.place(x=60,y=115)
		self.lblconcepto.configure(font=("arial",8,"bold"),bg='cornsilk')
		self.EntryConcepto=Entry(self.miFrameR)
		self.EntryConcepto.place(x=60,y=135)
		self.EntryConcepto.config(justify="center")

		self.btnIngreso = Button(self.raizR,text="Transferir", command=lambda: self.Transferencia())
		self.btnIngreso.place(x=60,y=215)

		self.btnCancelar = Button(self.raizR,text="Cancelar", command=lambda: self.Cancelar())
		self.btnCancelar.place(x=128,y=215)

		self.raizR.mainloop()
	
	def Transferencia(self):
		cue = Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0]
		retirada = int(self.EntryImport.get())* -1
		ingreso = int(self.EntryImport.get())
		cueTraspaso = Modelo.cuenta.loadCue(None,None,self.EntryNumCue.get())[0]

		try:
			if retirada<0 and 200+cue.saldo>=ingreso:
				Modelo.movimiento.crearMov(self.EntryConcepto.get(),cueTraspaso.saldo,cueTraspaso.saldo+int(ingreso),cueTraspaso.id,datetime.now().strftime('%Y-%m-%d'))
				Modelo.movimiento.crearMov(self.EntryConcepto.get(),cue.saldo,cue.saldo+int(retirada),cue.id,datetime.now().strftime('%Y-%m-%d'))
				self.raizR.destroy()
				cambiosDeCuenta()
			else:
				messagebox.showwarning("Error", "Saldo insuficiente")
		except:
			pass

	def Cancelar(self):
		self.raizR.destroy()

def Salir():
	respuesta=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
	if respuesta==True:
		raiz.destroy()

		import VistaIniSesion
		

# Barra menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

img_Micuenta = tk.PhotoImage(file="Recourses/Micuenta.png")
img_AdministrarCuentas = tk.PhotoImage(file="Recourses/administrarCuentas.png")

MenuMiCuenta = Menu(barraMenu, tearoff=0)
MenuMiCuenta.add_command(label="Datos personales", image=img_Micuenta, compound=tk.LEFT,command=VentanaDatosPersonales)
MenuMiCuenta.add_command(label="Administrar cuentas", image=img_AdministrarCuentas, compound=tk.LEFT, command=AdministrarCuentas)
barraMenu.add_cascade(label="Mi cuenta",menu=MenuMiCuenta)

barraMenu.add_command(label="Hacer un ingreso", command=VentanaHacerIngreso)

barraMenu.add_command(label="Sacar dinero", command=VentanaHacerRetirada)

barraMenu.add_command(label="Transferencia bancaria", command=VentanaHacerTransferencia)

barraMenu.add_command(label="Salir", command=Salir)

lblBienvenida = Label(miFrame, text="Te damos la bienvenida a tu Banca Online")
lblBienvenida.place(x=35,y=30)
lblBienvenida.configure(font=("arial",12,"bold"))
lblBienvenida.configure(bg='cornsilk')

#Combobox
clien= Modelo.cliente.loadCli(None,None,dni)[0]

listacuentas=Modelo.cuenta.loadCue(clien.id,None,None)
listacuentas2=[]
for i in range(len(listacuentas)):
	nombre=listacuentas[i].nombre
	listacuentas2.append(nombre)

TextMov=Text(miFrame)
scrollVert=Scrollbar(miFrame, command=TextMov.yview,width=14)
scrollVert.place(in_=TextMov, relx=1, relheight=1, bordermode="outside")
TextMov.place(x=35,y=170,width=480,height=200)
TextMov.configure(yscrollcommand=scrollVert.set, padx=10, pady=10, )


def cambiosDeCuenta():
	TextMov.configure(state=NORMAL)
	#lo que pasa cuadno se cambia de cuenta
	# cuenta select
	cuentaActual = Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0]
	# saldo de la cuenta
	lblsaldo['text'] = "Saldo actual de la cuenta: "+str(cuentaActual.saldo)
	# lista mov
	listaMovimientosSinOrdenar = Modelo.movimiento.loadMov(None,cuentaActual.id)
	listaMovimientos =  [num for num in reversed(listaMovimientosSinOrdenar)]

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
		
		anyo = Mov.fecha[:4]
		mes = Mov.fecha[5:7]
		dia = Mov.fecha[8:10]
		fecha = dia+"/"+mes+"/"+anyo
		TextMov.insert(INSERT, Mov.concepto +"- "+ Mov.saldoAnterior +"- "+ str(importe) +"- "+ str(Mov.saldoActual) +"- "+fecha + "\n")
	
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
	TextMov.configure(state=DISABLED)

combo = ttk.Combobox( state="readonly",
    values=listacuentas2)
combo.place(x=40, y=70)
combo.current(0)
def atajo(self):
	cambiosDeCuenta()
combo.bind("<<ComboboxSelected>>", atajo)

lblsaldo = Label(miFrame, text="Saldo actual de la cuenta: "+str(Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0].saldo))
lblsaldo.place(x=35,y=100)
lblsaldo.configure(font=("arial",12,"bold"))
lblsaldo.configure(bg='cornsilk')

lblUltimosMov = Label(miFrame, text="Últimos movimientos")
lblUltimosMov.place(x=35,y=140)
lblUltimosMov.configure(font=("arial",12,"bold"))
lblUltimosMov.configure(bg='cornsilk')

ingresos=0
gastos=0
cuentaActual = Modelo.cuenta.loadCue(clien.id,combo.get(),None)[0]
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
TextMov.configure(state=DISABLED)
raiz.mainloop()


		