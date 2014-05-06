 def onchange_calcular_edad(self,cr,uid,ids,fecha_nacimiento):
  res={'value':{}}
  anio=int(fecha_nacimiento[0:4])
  mes=int(fecha_nacimiento[5:7])
  dia=int(fecha_nacimiento[8:10])
  fecha_actual=datetime.datetime.now()
  fecha_nacimiento=datetime.datetime(anio,mes,dia)
  diff=  fecha_actual - fecha_nacimiento
  edad= diff.days/365
  res['value']['edad']=edad
  return res
