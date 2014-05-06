import datetime
 
def edad(fecha_nacimiento):
    # Obtenemos la fecha actual del Sistema
    ahora = datetime.datetime.utcnow()
    ahora = now.date()
 
    # Obtenemos la diferencia entre la fecha actual y la fecha de nacimiento
    edad = dateutil.relativedelta.relativedelta(ahora, fecha_nacimiento)
 
    #Podemos retornar la fecha en años(years)
    edad = edad.years
 
    return edad

print edad("1994/04/24")
