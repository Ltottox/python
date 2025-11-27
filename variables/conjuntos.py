#conjunto con set
conjunto=set(["antonio", "maria", "luis"])#crea un conjunto con elementos

#conjunto dentro de otro conjunto
conjunto_anidado=set([frozenset(["a", "b"]), frozenset(["c", "d"])])#frozenset es un conjunto inmutable 
print(conjunto)
print(conjunto_anidado)

#teoria de conjuntos y subconjuntos
# el conjunto con mas elementos es el conjunto principal
A=set([1, 2, 3, 4, 5])
B=set([1, 2, 3, 4])     #subconjunto de A
#C=set([4, 5, 6, 7, 8])  #conjunto C

resultado= A.issubset(B) #verifica si A es un subconjunto de B
print(f"el conjunto A es subconjunto de B: {resultado}")
resultado= A.issuperset(B) #verifica si A es un superconjunto de B
print(f"el conjunto A es superconjunto de B: {resultado}")
resultado= B.issubset(A) #verifica si B es un subconjunto de A
print(f"el conjunto B es subconjunto de A: {resultado}")
resultado= B.issuperset(A) #verifica si B es un superconjunto de A
print(f"el conjunto B es superconjunto de A: {resultado}")

print ("---------------------------------------------------")
#operaciones con conjuntos
print(f"Unión de A y B: {A.union(B)}")
print(f"Intersección de A y B: {A.intersection(B)}")
print(f"Diferencia de A y B: {A.difference(B)}")
print(f"Diferencia simétrica de A y B: {A.symmetric_difference(B)}")
print ("---------------------------------------------------")

# PARA VERIFICAR ELEMENTOS EN UN CONJUNTO EN COMUN
resultado= A.isdisjoint(B) #verifica si A y B no tienen elementos en comun
print(f"el conjunto A y B no tienen elementos en comun: {resultado}")


