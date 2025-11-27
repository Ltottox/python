 # iterar elementos de diferentes estructuras de datos
#ejemplo con lista
animales = ["perro", "gato", "pez", "pajaro"]
frutas = ["manzana", "banana", "cereza", "naranja"]
numeros = [1, 2, 3, 4, 5]

#RECORRER LISTA CON CONTINUE
for animal in animales:
    if animal == "gato":
        continue  #saltar el gato
    print(f"El animal es: {animal}")
print("---------------------------------------------------")

#EVITAR QUE EL BUCLE SE DETENGA CON BREAK
for animal in animales:
    if animal == "pez":
        break  #detener el bucle al encontrar pez
    print(f"El animal es: {animal}")
print("---------------------------------------------------")

#RECORRER UNA CADENA DE TEXTO
mensaje = "Hola Mundo"
for letra in mensaje:
    print(f"La letra es: {letra}")
print("---------------------------------------------------")

#for en una linea de codigo, sirve para crear listas rapidas, su sintaxis es: [expresion for item in iterable]  
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)