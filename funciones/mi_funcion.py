#crear ni propia funcion, con def creamos funciones reutilizables
def mi_funcion(nombre):
    print(f"Hola, {nombre}!")
    
#llamar a la funcion
mi_funcion("Antonio")

#fincin con parametro de retorno
def saludar(nombre):
    return f"Hola, {nombre}!"   
print(saludar("Maria"))
print("---------------------------------------------------")
#funcion con doble parametro
def saludar_doble(nombre, sexo):
    if sexo == sexo.lower() == "f" or sexo.lower() == "femenino":
        return f"Hola, Sra. {nombre}!"
    elif sexo == sexo.lower() == "m" or sexo.lower() == "masculino" :
        return f"Hola, Sr. {nombre}!"   
    else:
        return f"Hola, {nombre}!"   
print(saludar_doble("Luis", "m"))
print(saludar_doble("Ana", "femenino"))
print(saludar_doble("Alex", "otro"))
print("---------------------------------------------------")

#funcion que os retorna varios valores
#ejemplo crear una contraseña segura
import random   
def generar_contrasena(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))#generar una contrasena aleatoria de la longitud dada. el join une los caracteres en una sola cadena
    return contrasena, longitud #retorna la contrasena y su longitud, como una tupla, no se necesita usar parentesis para retornarlo como tupla y no se visualisa como tal
#para visualisar la contrasena y su longitud
contrasena, longitud = generar_contrasena(5)
print(f"Contraseña: {contrasena}, Longitud: {longitud}")
print("---------------------------------------------------")
#funcion con parametro por defecto
def potencia(base, exponente=2):
    return base ** exponente    
print(potencia(3)) #usa el exponente por defecto
print(potencia(2, 3)) #usa el exponente dado    
print("---------------------------------------------------")