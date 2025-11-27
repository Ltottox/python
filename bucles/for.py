#bucle for se usa para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena de texto).

#ejemplo con lista
animales = ["gato", "perro", "pez", "loro"]
for animal in animales:
    print(f"El animal es: {animal}")
print("---------------------------------------------------")

#ejemplo con lista de con su indice usando len() No es lo mas optimo
frutas = ["manzana", "banana", "cereza", "naranja"]
for i in range(len(frutas)):
    print(f"Fruta {i + 1}: {frutas[i]}")    
print("---------------------------------------------------")

#ejemplo con lista usando enumerate() es un metodo mas optimo
colores = ["rojo", "verde", "azul", "amarillo"]
for indice, color in enumerate(colores):
    print(f"Color {indice + 1}: {color}")
print("---------------------------------------------------")

#cuando el else se usa en un bucle for se ejecuta cuando el bucle termina normalmente (sin interrupciones).
for numero in range(3):
    print(f"El numero es: {numero}")
else:
    print("El bucle ha terminado.")
print("---------------------------------------------------")

#ejemplo con tupla
numeros = (1, 2, 3, 4, 5)               
for numero in numeros:
    print(f"El numero es: {numero}")
print("---------------------------------------------------")

#desempaquetado de tupla en bucle for
puntos = [(1, 2), (3, 4), (5, 6)]
for x, y in puntos:
    print(f"x: {x}, y: {y}")        
print("---------------------------------------------------")

#ejemplo de como iterar dos listas al mismo tiempo con zip(), debe tener la misma cantidad de elementos
nombres = ["Antonio", "Maria", "Luis"]  
edades = [30, 25, 28]
for nombre, edad in zip(nombres, edades):
    print(f"Nombre: {nombre}, Edad: {edad}")
print("---------------------------------------------------")
 
#ejemplo con diccionario
persona = {"nombre": "Antonio", "edad": 30, "ciudad": "Madrid"}
for clave in persona:
    print(f"{clave}: {persona[clave]}")
   
print("---------------------------------------------------")
#ejemplo con conjunto
colores = {"rojo", "verde", "azul"}
for color in colores:
    print(f"El color es: {color}")
print("---------------------------------------------------")
#ejemplo con cadena de texto
mensaje = "Hola Mundo"  
for letra in mensaje:
    print(f"La letra es: {letra}")
print("---------------------------------------------------")
#ejemplo con range()
for i in range(5):  #itera desde 0 hasta 4  
    print(f"El numero es: {i}")
print("---------------------------------------------------")

#ejemplo con range() con inicio y fin
for i in range(2, 7):  #itera desde 2 hasta 6   
    print(f"El numero es: {i}")
print("---------------------------------------------------")

#ejemplo con range() con paso
for i in range(1, 21, 3):  #itera desde 1 hasta 20 con paso de 3
    print(f"El numero es: {i}")
print("---------------------------------------------------")

#ejemplo con range() en orden inverso
for i in range(10, 0, -2):  #itera desde 10 hasta 1 con paso de -2  
    print(f"El numero es: {i}")
print("---------------------------------------------------")

#ejemplo de bucle for anidado
for i in range(1, 4):  #bucle externo
    for j in range(1, 4):  #bucle interno
        print(f"i: {i}, j: {j}")
print("---------------------------------------------------")

#ejemplo de bucle for con break
for i in range(10):
    if i == 5:
        print("Se encontró el numero 5, saliendo del bucle.")
        break  #sale del bucle cuando i es 5
    print(f"El numero es: {i}")
print("---------------------------------------------------")

#ejemplo de bucle for con continue
for i in range(10): 
    if i % 2 == 0:
        continue  #salta el resto del codigo cuando i es par
    print(f"El numero impar es: {i}")
print("---------------------------------------------------")
#ejemplo de bucle for con pass
for i in range(5):  
    if i == 3:
        pass  #no hace nada cuando i es 3
    print(f"El numero es: {i}")     
print("---------------------------------------------------")
#ejemplo de bucle for con else
for i in range(3):
    print(f"El numero es: {i}")
else:
    print("El bucle ha terminado.")
print("---------------------------------------------------")    

