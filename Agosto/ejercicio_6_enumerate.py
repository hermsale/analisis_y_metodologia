numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

posiciones = [i for i, numero in enumerate(numeros) if numero % 2 == 0]  # Encuentra posiciones de números pares
print(f"Las posiciones de los números pares son: {posiciones}")  # Muestra las posiciones encontradas




tridimencion = [
    [1, 2, 3],
    [[4, 5, 6], [7, 8, 9]],
    [[[10, 11], [12, 13]], [[14, 15], [16, 17]]]
    ]
print(f"El número en la posición [1][0][1] es: {tridimencion[1][0][1]}")  # Accede a un elemento específico