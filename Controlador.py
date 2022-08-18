import VistaIniSesion
import Modelo
from tkinter import messagebox


def identificarse():
	NIF=VistaIniSesion.EntryNIF.get()
	Clave=VistaIniSesion.EntryPass.get()

	cuentaAd=None
	i=0
	try:
		cuentaAd = Modelo.administrador.loadAdm(None,NIF,None)[0]	
		i=1
	except IndexError:
		pass


	if i==1 and cuentaAd.comprovarContra(Clave)==True:
			import VistaAppAdministrador

	else:
		cuentaCli=None
		try:
			cuentaCli = Modelo.cliente.loadCli(None,None,NIF)[0]	
		
			if cuentaCli.comprovarContra(Clave)==True:
				import VistaAppCliente
				
			else:
				messagebox.showwarning("Error", "Datos incorrectos")

		except IndexError:
			messagebox.showwarning("Error", "Datos incorrectos")
		except AttributeError:
			messagebox.showwarning("Error", "Datos incorrectos")
			
def abretuCuenta():
	VistaIniSesion.raiz.destroy()
	import VistaCrearCuenta
	

def CrearCuenta():
	import VistaCrearCuenta

	correcto=True
		
	nombre = VistaCrearCuenta.EntryNombre.get()
	apellidos = VistaCrearCuenta.EntryApellidos.get()
	dia = VistaCrearCuenta.EntryFechaNacimientoD.get()
	mes = VistaCrearCuenta.EntryFechaNacimientoM.get()
	anyo = VistaCrearCuenta.EntryFechaNacimientoA.get()
	fechaNacimiento = str(anyo)+"-"+str(mes)+"-"+str(dia)
	dni = VistaCrearCuenta.EntryDni.get()
	telefono = VistaCrearCuenta.EntryTelefono.get()
	clave = VistaCrearCuenta.EntryClave.get()
	
	if nombre.isalpha()==False or len(nombre)<1 or len(apellidos)<1:
		correcto=False
		messagebox.showwarning("Error", "Nombre o apellidos incorrectos")
	try:
		if len(str(dia))!=2 or len(str(mes))!=2 or len(str(anyo))!=4 or int(dia)<0 or int(dia)>31 or int(mes)>12 or int(mes)<0 or int(anyo)<1920 :
			raise ValueError("")

	except ValueError:
		correcto = False
		messagebox.showwarning("Error", "Fecha incorrecta dd-mm-aaaa")

	try:
		int(telefono)
		if len(telefono)>15:
			raise ValueError("")
	except ValueError:
	   	correcto = False
	   	messagebox.showwarning("Error", "El telfono tiene que ser un número y de cierta longitud")
	try:
		int(clave)
		if len(clave)>15:
			raise ValueError("")
	except ValueError:
	   	correcto = False
	   	messagebox.showwarning("Error", "La clave tiene que ser númerica y de cierta longitud")
	try:
		num=dni[:8]
		let=dni[8:9]

		int(num)
		if str.isdigit(let) == True:
			raise ValueError
		if len(dni)!=9:
			raise ValueError
	except ValueError:
		correcto = False
		messagebox.showwarning("Error", "Dni incorrecto")

	if correcto==True:
		
		Modelo.cliente.crearCliente(nombre,apellidos,fechaNacimiento,dni,telefono,clave)
		import VistaAppCliente


