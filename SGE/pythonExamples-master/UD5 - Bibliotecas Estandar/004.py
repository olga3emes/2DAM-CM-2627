from datetime import datetime, date, timedelta
# Fecha y hora actual
ahora = datetime.now()
print("Ahora:", ahora)
# Crear una fecha específica
cumple = date(2025, 7, 9)
print("Cumpleaños:", cumple)
# Sumar días
mañana = ahora + timedelta(days=1)
print("Mañana:", mañana.strftime("%Y-%m-%d %H:%M:%S"))

import time
# Hora actual en formato Unix (segundos desde 1970)
timestamp = time.time()
print("Timestamp actual:", timestamp)
# Pausar la ejecución por 2 segundos
print("Esperando...")
time.sleep(2)
print("¡Listo!")
# Formatear hora local
local = time.localtime()
print("Hora local formateada:", time.strftime("%H:%M:%S", local))

import calendar
# Mostrar el calendario de julio de 2025
print("Calendario julio 2025:")
print(calendar.month(2025, 7))
# Saber si un año es bisiesto
print("¿2024 es bisiesto?:", calendar.isleap(2024))
# Día de la semana (0=lunes, 6=domingo)
dia = calendar.weekday(2025, 7, 9)
print("Día de la semana (9 julio 2025):", calendar.day_name[dia])
