# Un diccionario en Pythyon es una colección de elementos, donde cada uno tiene una llave Key y un valor Value.
# Los diccionarios se pueden crear con parentesis {} separando con una coma cada par key:value
# Los diccionarios son mutables, es decir, se pueden modificar una vez creados.
# Se pueden crear diccionarios con un solo elemento, pero hay que poner una coma al final

mi_diccionario = {
    'Nombre': 'Juan',
    'Edad': 30,
    'Genero' : 'Masculino',
    'Ciudad': 'Buenos Aires'
}

print(mi_diccionario)  # imprime el diccionario completo
print(type(mi_diccionario))  # imprime el tipo del diccionario
print(mi_diccionario['Nombre'])  # imprime el valor asociado a la llave 'Nombre'