fecha = input("Introduzca una fecha (dd/mm/aaaa): ")

# divido la fecha en partes usando el separador "/"
fecha_split = fecha.split("/") 

# diccionario de meses
meses = {
    '01' : "Enero",
    '02' : "Febrero",
    '03' : "Marzo",
    '04' : "Abril",
    '05' : "Mayo",
    '06' : "Junio",
    '07' : "Julio",
    '08' : "Agosto",
    '09' : "Septiembre",
    '10' : "Octubre",
    '11' : "Noviembre",
    '12' : "Diciembre"
    }

# Inicializa la variable mes
mes = "Mes no válido"

# Verifica si el mes ingresado está en el diccionario y asigna su valor
if fecha_split[1] in meses:
    mes = meses[fecha_split[1]]

print(f"Fecha ingresada:", fecha_split[0], "de", mes, "de", fecha_split[2])  # imprime la fecha formateada
