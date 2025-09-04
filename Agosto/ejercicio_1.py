personas = []
# Ejercicio 1: Crear un diccionario con datos de una persona y mostrar un mensaje formateado

for i in range(2):  # Repite 3 veces para crear 3 personas
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    genero = input("Introduce tu género (M/F): ")

    mi_diccionario_persona = {
        'Nombre': nombre,
        'Apellido': apellido,
        'Genero': genero
    }

    personas.append(mi_diccionario_persona)  # Agrega el diccionario de la persona a la lista

# asi se formatea una cadena con f-strings 
for persona in personas:
    print(f"Hola {persona['Nombre']} {persona['Apellido']}, tu género es {persona['Genero']}.")