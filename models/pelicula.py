# -*- coding: utf-8 -*-

from osv import osv,fields

class pelicula(osv.Model):
	_name= 'gidsoft.peliculas.pelicula'
	_rec_name='nombre_pelicula'

	_columns={
		'cod_pelicula':fields.char('Codigo Pelicula', required=True, size=4),
		'nombre_pelicula':fields.char('Nombre Pelicula', size=42),
		'sinopsis':fields.text('Sinopsis de la Pelicula'),
		'director_id':fields.many2one('gidsoft.peliculas.director', 'Director'),
		'autor_id':fields.many2one('gidsoft.peliculas.autor', 'Autor'),
		'genero_id':fields.many2one('gidsoft.peliculas.genero', 'Genero'),
		'ano_estreno':fields.date('Año de Estreno'),
		'imagen':fields.binary('Imagen', filtars='*.png, *.gif')
	}