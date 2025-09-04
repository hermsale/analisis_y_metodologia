
while True:
    cantidad = int(input("¿Cuántos números queres ingresar? (mínimo debe ser 5) "))
    if cantidad >= 5:   # condición de salida
        break
    print("⚠️ Debes ingresar al menos 5 números.")

acumulador = 0
for i in range(cantidad):  
    numero = int(input("Introduce un número: "))
    acumulador = acumulador + numero  # Suma el número al acumulador

print(f"La suma de los números ingresados es: {acumulador}")
print(f"El promedio de los números ingresados es: {acumulador / cantidad if cantidad > 0 else 0}")

