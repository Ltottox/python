frase= input( "dime una frase y te calculo cuanto demoras en decirla")
longitud_frase= len(frase)
tiempo_decir_frase= longitud_frase / 15 #suponiendo que una persona promedio habla 15 caracteres por segundo
print(f"tu frase tiene {longitud_frase} caracteres y demoras {tiempo_decir_frase} segundos en decirla") 