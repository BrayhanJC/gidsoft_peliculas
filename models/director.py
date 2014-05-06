# -*- coding: utf-8 -*-

from osv import osv,fields
from datetime import *

class director(osv.Model):
	_name='gidsoft.peliculas.director'

	cbo_sexo=[
		('m', 'Masculino'),
		('f', 'Femenino')
	]

	cbo_pais=[('co', 'Colombia'),
		('es', 'España'),
		('usa', 'Estados Unidos'),
		('ve', 'Venezuela'),
		('eg', 'Egipto')
	]

	_columns= {
		'identificacion_director':fields.char('Identificacion', required=True, size=10),
		'name':fields.char('Nombres', size=32),
		'ape_director':fields.char('Apellidos', size=32),
		'fecha_nacimiento':fields.date('Fecha de nacimiento'),
		'edad':fields.integer('Edad', size=3),
		'sexo':fields.selection(cbo_sexo, 'Sexo'),
		'pais':fields.selection(cbo_pais, 'Pais de origen')
	}

	def onchange_calcular_edad(self,cr,uid,ids, fecha_nacimiento):
		#self = Es como un this
		#cr = Es el cursor de la base de datos, conexion a la base de datos
		#uid = Id del usuario que esta haciendo la operacion
		#ids = 
	  """
	  Retorna la edad en anios.
	  """
	  res={'value':{}}
	  d = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), "%Y-%m-%d") - datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
	  res['value']['edad']=d
	  return res
