# las tuplas son inmutables
# no se pueden modificar una vez creadas. son una colección de datos ordenados que encierran sus elementos con parentesis
# se pueden crear tuplas con un solo elemento, pero hay que poner una coma al final

t=('uno', 2,'tres', 4.5 ,'cinco') # una tupla con 5 elementos

a, b, c, d, e = t  # desempaquetado de tuplas 

print(a)
print(b)
print(c)
print(d)
print(e)

print(t[0]) # imprime el primer elemento de la tupla

print(type (t[1])) # imprime el tipo del segundo elemento de la tupla
print(t[1:3])  # imprime los elementos desde el índice 1 hasta el 2 (el 3 no se incluye)

print(type (t[0])) # imprime el tipo del primer elemento de la tupla