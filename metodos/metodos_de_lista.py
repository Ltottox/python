#creando lista con list()
lista= list(["hola", "pablo", 26,25,"gato"])

# len, deviuelve cantidad de elemntos de la lista 
cantidad_elemntos= len(lista)

#append, agrega un elemento  al final de la lista 
lista.append("avion")#['hola', 'pablo', 26, 25, 'gato', 'avion']

#insert, agraga un elemento a la lista en un indice especifico
lista.insert(2,"martillo")#['hola', 'pablo', 'martillo', 26, 25, 'gato', 'avion']

#extend agregamos varios elemntos a la lista con otra lista
lista.extend(["agua",True])#['hola', 'pablo', 'martillo', 26, 25, 'gato', 'avion', 'agua', True]

#pop, elimina eementos or su indice
lista.pop(4)#['hola', 'pablo', 'martillo', 26, 'gato', 'avion', 'agua', True] se limino 25

#remove unn elemento por su valor no por indice
lista.remove("avion")#['hola', 'pablo', 'martillo', 26, 'gato', 'agua', True

#sort ordena elemnto de forma asc
lista.sort( )


#reverse , invierte elementos en una lista
lista.reverse()

# lista.clear()



print(lista)