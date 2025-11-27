diccionario = {
    "nombre" : 'toto',
    "apellido": 'saldivia',
    "edad" : 42
}
#otra forma de crear diccionarios
diccionario_alt = dict(nombre='toto', apellido='saldivia', edad=42)
print(diccionario) #comprobar que ambos diccionarios son iguales
print(diccionario_alt)  
print("---------------------------------------------------")

#keys develve un objeto dic_item
claves = diccionario.keys()

#creaando un diccionario con las fromkeys, asignando un valor predeterminado a todas las claves
diccionario_fromkeys = dict.fromkeys(claves, "valor_predeterminado")
print(diccionario_fromkeys)
print("---------------------------------------------------")    

#get obtiene un elemento con get() 
valor_de_kaka = diccionario.get("kaka")
print("el programa continua")

#pop elimna elemnto del diccionario
diccionario.pop("edad") #elimina clave

#item, obtiene un elemneto del diccionaro iterables
diccionario_i = diccionario.items()

#clear elimina todo del diccionario usar con responsabilidad
#diccionario.clear()

print(diccionario)
print("---------------------------------------------------")

#CREANDO DICCCIONARIOS USANDO DICT()
diccionario2 = dict(nombre="antonio", apellido="saldivia", edad=30)
print(diccionario2)
print("---------------------------------------------------")

#la lista no pueden ser claves y usamos frozenset para crear claves inmutables
diccionario3 = {
    frozenset(["a", "b"]) : "valor1",
    frozenset(["c", "d"]) : "valor2"
}
print(diccionario3)
print("---------------------------------------------------")

#creando diccionarios con fromkeys con none como valor predeterminado el primer dato es iterable 
diccionario4 = dict.fromkeys(["nombre", "apellido", "edad"])
print(diccionario4)
print("---------------------------------------------------")
# si le pasamos solo una cadena de texto lo toma como iterable y crea una clave por cada letra
diccionario5 = dict.fromkeys("abcde")
print(diccionario5)
print("---------------------------------------------------")
# si le pasamos un segundo parametro asigna ese valor a todas las claves
diccionario6 = dict.fromkeys(["nombre", "apellido", "edad"], "desconocido")
print(diccionario6)
print("---------------------------------------------------")

#ejemplo de uso de diccionario
persona = {
    "nombre": "Luis",   
    "edad": 28,
    "ocupacion": "medico",
}                               
nombre = persona.get("nombre")
edad = persona.get("edad")
ocupacion = persona.get("ocupacion")    
print(f"Nombre: {nombre}, Edad: {edad}, Ocupacion: {ocupacion}")
print("---------------------------------------------------")