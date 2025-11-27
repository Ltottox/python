#listas
lista=["antonio ", 30, "estudiante", 1.72]#conjunto de datos comienza desde el indice 0


#tuplas igual a las listas pero con parentecis( no se puede modificar su dato)
tupla=("antonio ", 30, "estudiante", 1.72)


# creando un conjunto set
conjunto={"antonio ", 30, "estudiante", 1.72}# en un conjunto no habra datos duplicados, va con {}no se puee llar por su indice, son datos desordenados

#creando un diccionario. es como JSON. y se define por clave: valor
diccionario={
    'nombre' : "Antonio",
    'edad' : 42,
    'ocupacion' : "estudiante",
    'estatura' : 1.72
    
}

print(lista[2])# resultado esudiante
print(tupla[2])# resultado estudiante, se llama con corchetes tambien
print(conjunto)
print(diccionario["edad"])# resultado se llama por la clave 


