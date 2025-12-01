#Lambda crea funciones anonimas de una sola linea
#sintaxis: lambda parametros: expresion

#ejemplo 1: funcion lambda que suma dos numeros. se retorna el resultado de la suma automaticamente
suma = lambda x, y: x + y #x e y son parametros, x + y es la expresion
print(suma(3, 5)) #llama a la funcion lambda con argumentos 3 y 5, devuelve 8    
print("---------------------------------------------------")

#ejemplo 2: funcion lambda que verifica si un numero es par
es_par = lambda n: n % 2 == 0 #n es el parametro, n % 2 == 0 es la expresion que retorna True si n es par
print(es_par(4)) #llama a la funcion lambda con argumento 4, devuelve True
print(es_par(7)) #llama a la funcion lambda con argumento 7, devuelve False
print("---------------------------------------------------")

# ejemplo co la funcin filter() y lambda para filtrar numeros pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros )) #filter aplica la funcion lambda a cada elemento de la lista numeros
print(numeros_pares) #devuelve [2, 4, 6]

numeros_inpares = list(filter(lambda x: x % 2 != 0, numeros )) #filter aplica la funcion lambda a cada elemento de la lista numeros
print(numeros_inpares) #devuelve [1, 3, 5]  
print("---------------------------------------------------") 

# ejemplo con la funcion map() y lambda para elevar al cuadrado cada numero de una lista
numeros_cuadrados = list(map(lambda x: x ** 2, numeros)) #map aplica la funcion lambda a cada elemento de la lista numeros
print(numeros_cuadrados) #devuelve [1, 4, 9, 16, 25, 36]
print("---------------------------------------------------")
