cadena1 ="hola, soy, antonio"
cadena2 = "hola"

#dir (es unna funcion)
#print(dir(cadena1)) #muestra todos los metodos q puede hacer
#dato.metodo()

#mayus
mayus = cadena1.upper()
#minus
minus= cadena1.lower()
#capitalize
capit = cadena1.capitalize()

#find . busca una cadena en otra cadena, si no hay coincidencia lanza -1
busqueda_find = cadena1.find("s") #resutado 5

#index . busca una cadena en otra cadena, si no hay coincidencia lanza excepcion
busqueda_index = cadena1.index("l")

#isnumeric , tru o false
es_numerico = cadena2.isnumeric()

#isalfa, si es alfa solo letras de la a-z es tru sino es false
es_alfa = cadena2.isalpha()

#count: #find . busca una cadena en otra cadena,devuelve la cantidad de veces que coincida, si no la encuuetra el resultado es 0
contar_coincidencias = cadena1.count("a")# pude ser texto

#len,  contamos cuanto caracteres tiene una cadena
contar_caracteres = len(cadena2)

#startswith, verifica si una cadena comienza con otra cadena dada
empieza_con= cadena1.startswith("h")

#endswith, verifica si una cadena comienza con otra cadena dada
termina_con= cadena1.endswith("f")

#replace, remplaza un edazi de la cadena por otra dada 
remplaza_cadena=cadena1.replace("la","looo")

#split, devuleve una lista , separa cadenas con el parametro que le pasemos
cadena_separada= cadena1.split("o")

print(cadena_separada)