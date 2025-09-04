numeros = [3, 5, 2, 8, 6]

numMayor = numeros[0]  # Asumimos que el primer número es el mayor
for numero in numeros:
        if numero > numMayor:  # Comparamos cada número con el mayor encontrado
            numMayor = numero  # Actualizamos el mayor si encontramos uno más grande

print(f"El número mayor es: {numMayor}")  # Mostramos el número mayor encontrado