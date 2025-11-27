numeros = [4,8,15,16,23,42 ]

#encontrar el numeros mayor en la lista
mayor = max(numeros)
print(f"El número mayor es: {mayor}")

#encontrar el numero menor en la lista
menor = min(numeros)    
print(f"El número menor es: {menor}")

#redondear un numero decimal
decimal = 3.14159
redondeado = round(decimal, 2)#redondea a 2 decimales
print(f"El número redondeado es: {redondeado}")
print("---------------------------------------------------")


#funcion bool() convierte un valor a booleano
#si retorna falce-> 0, vacio, None, False
#si retorna true-> cualquier otro valor diferente a los anteriores  

#ejemplo con 0
valor1 = 0
booleano1 = bool(valor1)
print(f"El valor {valor1} convertido a booleano es: {booleano1}")

#ejemplo con cadena vacia
#retorna False porque la cadena vacia es considerada falsa
valor2 = "  "
booleano2 = bool(valor2)    
print(f"El valor '{valor2}' convertido a booleano es: {booleano2}")

#ejemplo con lista vacia
#retorna False porque la lista vacia es considerada falsa
valor3 = []
booleano3 = bool(valor3)
print(f"El valor {valor3} convertido a booleano es: {booleano3}")

#ejemplo con None
#retorna False porque None es considerado falso
valor4 = None
booleano4 = bool(valor4)
print(f"El valor {valor4} convertido a booleano es: {booleano4}")

#ejemplo con numero diferente de 0
#retorna True porque cualquier numero diferente de 0 es considerado verdadero
valor5 = 10
booleano5 = bool(valor5)
print(f"El valor {valor5} convertido a booleano es: {booleano5}")   

#ejemplo con cadena no vacia
#retorna True porque cualquier cadena no vacia es considerada verdadera
valor6 = "Hola"
booleano6 = bool(valor6)
print(f"El valor '{valor6}' convertido a booleano es: {booleano6}") 

#ejemplo con lista no vacia
#retorna True porque cualquier lista no vacia es considerada verdadera
valor7 = [1, 2, 3]
booleano7 = bool(valor7)
print(f"El valor {valor7} convertido a booleano es: {booleano7}")
print("---------------------------------------------------")

#funcion all() devuelve True si todos los elementos del iterable son verdaderos o si el iterable está vacío
datos1 = [1, 2, 3, 4, 5]
resultado1 = all(datos1)       
print(f"Todos los elementos de {datos1} son verdaderos: {resultado1}")
datos2 = [1, 0, 3, 4, 5]
resultado2 = all(datos2)
print(f"Todos los elementos de {datos2} son verdaderos: {resultado2}")
print("---------------------------------------------------")

#funcion sum() suma todos los elementos de un iterable
numeros_a_sumar = [10, 20, 30, 40, 50]
suma_total = sum(numeros_a_sumar)
print(f"La suma total de {numeros_a_sumar} es: {suma_total}")   