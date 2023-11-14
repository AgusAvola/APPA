import datetime
hora_actual=datetime.datetime.now()
hora_formateada = hora_actual.strftime('%H:%M')

from threading import Event
print("esperando")
Event().wait(2)
print("termino la espera")
print(hora_formateada)
print(datetime.date.today().strftime('%A'))
print(hora_actual.strftime('%d/%m/%y'))
print(hora_actual.strftime('%y/%m/%d %H:%M'))