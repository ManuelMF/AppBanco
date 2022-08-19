import sqlite3
# Abrir / Crear una conexion
miConexion=sqlite3.connect("BD_Banco.db")

miCursor=miConexion.cursor()


miConexion.commit() 


miConexion.close()

class movimiento():
	def __init__(self,idd,concepto,saldoAnterior,saldoActual,cuentaid,fecha):
		self.id=idd
		self.concepto=concepto
		self.saldoAnterior=saldoAnterior
		self.saldoActual=saldoActual
		self.cuentaid=cuentaid
		self.fecha=fecha
	@staticmethod
	def crearMov(concepto,saldoAnterior,saldoActual,cuentaid,fecha):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		miCursor.execute("INSERT INTO movimientos VALUES (NULL,?,?,?,?,?)", (concepto,saldoAnterior,saldoActual,cuentaid,fecha))

		miConexion.commit() 
		miConexion.close()

	@staticmethod
	def loadMov(concepto,cuentaid):
		'''
		Devueve una lista
		Carga todos los movimientos con none none
		Carga con una busqueda con el concepto
		Carga con id con cuentaid 
		'''
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()
		select="select * from movimientos where 1=1 "
		if concepto != None:
			select=select+"and mov_concepto like '"+concepto+"%' "
		if cuentaid != None:
			select=select+"and mov_codcue = "+str(cuentaid)+" "
	
		miCursor.execute(select)

		movimientos=miCursor.fetchall()
		lista=[]
		for i in range(len(movimientos)):
			mov = movimiento(movimientos[i][0],movimientos[i][1],movimientos[i][2],movimientos[i][3],movimientos[i][4],movimientos[i][5])
			lista.append(mov)

		miConexion.commit() 
		miConexion.close()

		return lista

class cuenta():
	def __init__(self,id,nombre,saldo,fechaCreacion,clienteid):
		self.id=id
		self.nombre=nombre
		self.saldo=saldo
		self.fechaCreacion=fechaCreacion
		self.clienteid=clienteid

	@staticmethod
	def crearCuenta(nombre,saldo,FechaCreacion,codcliente):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		miCursor.execute("INSERT INTO cuentas VALUES (NULL,?,?,?,?)", (nombre,saldo,FechaCreacion,codcliente))

		
		miConexion.commit() 
		
		miConexion.close()
		cuen=cuenta(miCursor.lastrowid,nombre,saldo, FechaCreacion,codcliente)
		return cuen


	def borrarCuenta(self):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()
		
		miCursor.execute("delete from cuentas where cue_codcue='"+str(self.id)+"'")

		miConexion.commit() 
		miConexion.close()
	
	def updateContra(self,clave):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		miCursor.execute("update cuentas set cue_contrasenya='"+ clave +"' where cue_codcue='"+str(self.id)+"'")

		miConexion.commit() 
		
		miConexion.close()
	
	@staticmethod
	def loadCue(codCliente,nombre):
		'''
		Devueve una lista
		Carga todas las cuentas con none none
		Carga con una busqueda con el nombre
		Carga con id el cliente 
		'''
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()
		select="select * from cuentas where 1=1 "
		if nombre != None:
			select=select+"and cue_nombre like '"+nombre+"%' "
		if codCliente != None:
			select=select+"and cue_codcli = "+str(codCliente)+" "
		
		miCursor.execute(select)
		
		cuentas=miCursor.fetchall()
		
		lista=[]
	
		for i in range(len(cuentas)):
			cue = cuenta(cuentas[i][0],cuentas[i][1],cuentas[i][2],cuentas[i][3],cuentas[i][4])
			lista.append(cue)

		miConexion.commit() 
		miConexion.close()

		return lista
class cliente():
	def __init__(self,id,nombre,apellidos,fechaNacimiento,dni,telefono,clave):
		self.id=id
		self.nombre=nombre
		self.apellidos=apellidos
		self.fechaNacimiento=fechaNacimiento
		self.dni=dni 
		self.telefono=telefono
		self.clave=clave
	@staticmethod
	def crearCliente(nombre,apellidos,fechaNacimiento,dni,telefono,clave):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		miCursor.execute("INSERT INTO clientes VALUES (NULL,?,?,?,?,?,?)", (nombre,apellidos,fechaNacimiento,dni,telefono,clave))

		miConexion.commit() 
		
		miConexion.close()
		cli=cliente(miCursor.lastrowid,nombre,apellidos, fechaNacimiento,dni,telefono,clave)
		return cli

	def borrarCliente(self):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()
		
		miCursor.execute("delete from clientes where cli_codcli='"+str(self.id)+"'")

		miConexion.commit() 
		miConexion.close()

	def updateCliente(self,nombre,apellidos,fechaNacimiento,dni,telefono):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		miCursor.execute("update clientes set cli_nombre='"+ nombre +"', cli_apellidos='"+ apellidos +"', cli_FechaNacimiento='"+ fechaNacimiento +"', cli_dni='"+ dni +"', cli_telefono='"+ telefono +"'  where cli_codcli='"+str(self.id)+"'")

		miConexion.commit() 
		
		miConexion.close()

	@staticmethod
	def loadCli(codCliente,nombre,dni):
		'''
		Devueve una lista
		Carga todos los clientes con none none
		Carga con una busqueda con el nombre
		Carga con id el cliente 
		'''
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()
		select="select * from clientes where 1=1 "
		if nombre != None:
			select=select+"and cli_nombre like '"+nombre+"%' "
		if codCliente != None:
			select=select+"and cli_codcli = "+str(codCliente)+" "
		if dni != None:
			select=select+"and cli_dni = '"+dni+"' "
	
		miCursor.execute(select)

		clientes=miCursor.fetchall()

		lista=[]
		for i in range(len(clientes)):
			cli = cliente(clientes[i][0],clientes[i][1],clientes[i][2],clientes[i][3],clientes[i][4],clientes[i][5],clientes[i][6])
			lista.append(cli)

		miConexion.commit() 
		miConexion.close()

		return lista

	def comprovarContra(self,contra):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		try:
			miCursor.execute("select * from clientes where cli_codcli = "+str(self.id)+" and cli_clave = "+contra)
		except sqlite3.OperationalError:
			return False

		clientes=miCursor.fetchall()

		miConexion.commit() 
		miConexion.close()

		if len(clientes) == 0 :
			return False
		else: 
			return True

class administrador():
	def __init__(self,id,nombre,NIF,clave):
		self.id=id 
		self.nombre=nombre
		self.NIF=NIF 
		self.clave=clave

	@staticmethod
	def crearAdministrador(nombre,dni,clave):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		miCursor.execute("INSERT INTO administradores VALUES (NULL,?,?,?)", (nombre,dni,clave))

		miConexion.commit() 
		
		miConexion.close()
		ad=administrador(miCursor.lastrowid,nombre,dni,clave)
		return ad

	def borrarAdmin(self):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()
		
		miCursor.execute("delete from administradores where adm_codadm='"+str(self.id)+"'")

		miConexion.commit() 
		miConexion.close()

	def updateAdmin(self,nombre,clave):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		miCursor.execute("update administradores set adm_nombre='"+ nombre +"', adm_clave='"+ clave +"' where adm_codadm ='"+str(self.id)+"'")

		miConexion.commit() 
		
		miConexion.close()

	@staticmethod
	def loadAdm(id,NIF,nombre):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()
		select="select * from administradores where 1=1 "
		if nombre != None:
			select=select+"and adm_nombre like '"+nombre+"%' "
		if id != None:
			select=select+"and adm_codadm = "+str(id)+" "
		if NIF != None:
			select=select+"and adm_NIF like '"+str(NIF)+"' "

		miCursor.execute(select)

		administradores=miCursor.fetchall()

		lista=[]
		for i in range(len(administradores)):
			adm = administrador(administradores[i][0],administradores[i][1],administradores[i][2],administradores[i][3])
			lista.append(adm)

		miConexion.commit() 
		miConexion.close()

		return lista

	def comprovarContra(self,contra):
		miConexion=sqlite3.connect("BD_Banco.db")
		miCursor=miConexion.cursor()

		try:
			miCursor.execute("select * from administradores where adm_codadm = "+str(self.id)+" and adm_clave = "+contra)
		except sqlite3.OperationalError:
			return False

		administradores=miCursor.fetchall()

		miConexion.commit() 
		miConexion.close()

		if len(administradores) == 0 :
			return False
		else: 
			return True






#administrador.crearAdministrador("Paula","36985412Z",1234)
#lista=administrador.loadAdm(None,None,"Paul")
#ad=lista[0]
#adm=administrador(ad[0],ad[1],ad[2],ad[3])
#adm.borrarAdmin()

#cue=cuenta.loadCue(1,None)[0]
#print(cue.saldo)

#cliente.crearCliente("Sandra","Felix Morcillo","1990-05-03","48753264A",601879865,1234)
#cuenta.crearCuenta("Viaje a Andorra","600","2022-04-05",3)
#nombre,apellidos,fechaNacimiento,dni,telefono,clave

