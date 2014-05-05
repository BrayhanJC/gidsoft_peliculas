# -*- coding: utf-8 -*-

from osv import osv,fields

class director(osv.Models):
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