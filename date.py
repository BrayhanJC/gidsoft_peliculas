import datatime

def edad(self,cr,uid,ids, fecha_nacimiento):
	#self = Es como un this
	#cr = Es el cursor de la base de datos, conexion a la base de datos
	#uid = Id del usuario que esta haciendo la operacion
	#ids = 
  """
  Retorna la edad en anios.
  """
  d = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), "%Y-%m-%d") - datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
  return  d.days / 365