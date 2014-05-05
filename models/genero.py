# -*- coding: utf-8 -*-

from osv import osv, fields

class genero():
	_name='gidsoft.peliculas.genero'
	_columns={
		'cod_genero':fields.char('Codigo Pelicula', required=True, size=3),
		'name':fields.char('Genero', size=32)
	}