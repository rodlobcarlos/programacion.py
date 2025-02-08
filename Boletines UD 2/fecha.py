import datetime

hoy = datetime.datetime.today()
dia = hoy.day
mes = hoy.month
año = hoy.year
hora = hoy.hour
minutos = hoy.minute

nuevo_dia = hoy + datetime.timedelta(days = 5)