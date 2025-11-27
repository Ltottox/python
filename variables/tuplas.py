#funcion
def desempaquetar_tupla(tupla):
    nombre, edad, ocupacion, altura = tupla
    print(f"Nombre: {nombre}, Edad: {edad}, Ocupacion: {ocupacion}, Altura: {altura}")
#ejemplo de uso
mi_tupla = ("Antonio", 30, "estudiante", 1.72)
desempaquetar_tupla(mi_tupla)   

#ejemplo con tupla
tupla = ("Maria", 25, "ingeniera", 1.65)    
desempaquetar_tupla(tupla)

#con parametros de una lista si parentesis
tupla2 = "Luis", 28, "medico", 1.80 

print("\nDesempaquetado de tupla2:")
desempaquetar_tupla(tupla2) 