#funcion con parametro args
#el parametro *args permite pasar un numero variable de argumentos a una funcion
def suma(*numeros):
    return sum(numeros)

print(suma(1, 2, 3)) #tupla (1,2,3) devuelve 6
print(suma(4, 5))
print(suma(6))
#que se almacene en una variable tupla
resultado = suma(10, 20, 30, 40, 50)
print(resultado)
print("---------------------------------------------------")

#para mostrar una lista como argumentos individuales se usa el operador *
numeros_lista = [1, 2, 3, 4, 5]
print(suma(*numeros_lista)) #devuelve 15
print("---------------------------------------------------")

#ejemplo con mezcla de parametros normales y *args
def mostrar_info(nombre, *args):#nombre es un parametro normal y args es un parametro variable
    print(f"Nombre: {nombre}")
    print("Otros argumentos:")
    for arg in args:
        print(arg)  
mostrar_info("Antonio", 25, "Madrid", "Programador")#llama a la funcion con varios argumentos
print("---------------------------------------------------")