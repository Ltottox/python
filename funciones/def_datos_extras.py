def frase (nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, bienvenido al curso de python {adjetivo}"
#llamando a la funcion
print(frase("Antonio","Saldivia","avanzado"))

#llamando a la funcion forzando parametros
print(frase(adjetivo="intermedio",apellido="Saldivia",nombre="Antonio"))
print
#llamando a la funcion con parametros opcionales
def frase_opcional (nombre,apellido,adjetivo="avanzado"):#parametro adjetivo es opcional
    return f"hola {nombre} {apellido}, bienvenido al curso de python {adjetivo}"

print(frase_opcional("Antonio","Saldivia"))#usa el valor por defecto
print(frase_opcional("Antonio","Saldivia","intermedio"))#usa el valor dado