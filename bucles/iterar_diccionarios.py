#recorrer un diccionario
diccionario = {
    "nombre": "Antonio",
    "edad": 30,
    "ciudad": "Madrid"
}

#recorrer claves y valores
for clave, valor in diccionario.items():
    print(f"la clave es: {clave}, y el valor es: {valor}")
print("---------------------------------------------------")

#recorrer solo las claves
for clave in diccionario.keys():
    print(f"La clave es: {clave}")  
print("---------------------------------------------------")
#recorrer solo los valores
for valor in diccionario.values():      
    print(f"El valor es: {valor}")
print("---------------------------------------------------")

#recorrer diccionario con continue, sirve para saltar una iteracion
for clave, valor in diccionario.items():
    if clave == "edad":
        continue
    print(f"la clave es: {clave}, y el valor es: {valor}")
print("---------------------------------------------------")

#para detener un bucle usamos break
for clave, valor in diccionario.items():
    if clave == "edad":
        break
    print(f"la clave es: {clave}, y el valor es: {valor}")
    print("se detuvo el bucle edad con break")
print("---------------------------------------------------")

#recorrer un cadena de texto con for
mensaje = "Hola Mundo"
for letra in mensaje:
    print(f"La letra es: {letra}")
print("---------------------------------------------------")

#for en una linea de codigo, sirve para crear listas rapidas, su sintaxis es: [expresion for item in iterable]  
numeros_duplicados = [x * 2 for x in range(5)]
print(numeros_duplicados)

#recorrer diccionario con desempaquetado, sirve para diccionarios anidados
personas = {
    "persona1": {"nombre": "Antonio", "edad": 30},
    "persona2": {"nombre": "Maria", "edad": 25},
    "persona3": {"nombre": "Luis", "edad": 28}
}
for clave, valor in personas.items():
    print(f"la clave es: {clave}, y el valor es: {valor}")
print("---------------------------------------------------")
