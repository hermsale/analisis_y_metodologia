producto = []


def crear_juguetes():
    for i in range(1): 
        cantidad_payasos = input("¿Cuántos payasos quieres agregar? ")
        cantidad_munecas = input("¿Cuántas muñecas quieres agregar? ")

        mi_juguete = {
            'Payaso': cantidad_payasos,
            'Muñeca': cantidad_munecas
        }

        producto.append(mi_juguete)  # Agrega el diccionario del juguete a la lista

# defino una función para mostrar los juguetes
def mostrar_juguetes(producto):
    for juguete in producto:
        print(f"Payasos: {juguete['Payaso']}, Muñecas: {juguete['Muñeca']}")

def calcular_peso():
    peso_payaso = 0.112 # Peso de un payaso en kg
    peso_muneca = 0.75  # Peso de una muñeca en kg

    peso_total_payaso = peso_payaso * int(producto[0]['Payaso'])  # Obtiene la cantidad de payasos
    peso_total_muneca = peso_muneca * int(producto[0]['Muñeca'])
    peso_total = peso_total_payaso + peso_total_muneca  # Suma los pesos de payasos y muñecas

    print(f"El peso total de los juguetes es: {round(peso_total,2)} kg")


crear_juguetes()  # Llama a la función para crear los juguetes
# mostrar_juguetes(producto)  # Muestra los juguetes creados nuevamente


calcular_peso()  # Llama a la función para calcular el peso total de los juguetes