#curso que se demoran

#defino variable
otros_cursos_min = 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
curso_de_dalto =1.5

#video en bruto y duracion
bruto_promedio = 5
bruto_dalto = 3.5
#diferencias de video en bruto
diferencia_bruto_min = 100 - bruto_dalto / bruto_promedio * 100
diferencia_bruto_max = 100 - bruto_dalto / bruto_promedio * 100
print(f"el video en bruto de dalto dura un {diferencia_bruto_min}% menos que el promedio")
print(f"el video en bruto de dalto dura un {diferencia_bruto_max}% menos que el maximo")
print("---------------------------------------------------")

#diferencias de video en bruto
diferencia_si_editar_promedio =100 - ((otros_cursos_promedio * 1000 )// bruto_promedio) /10
tiempo_sin_editar_video= 100 - (curso_de_dalto*1000 // bruto_dalto)/10

print(f"el curso promedio de dalto elimina un {tiempo_sin_editar_video}% del video en bruto")
print(f"un curso promedio elimina un {diferencia_si_editar_promedio}% del video en bruto")
print("---------------------------------------------------")    

# diferencias de duracion
#primero se ejecutan las * / + -
diferencia_con_min = 100 - curso_de_dalto / otros_cursos_min * 100
# como el resultado arroja muchos decimales se ocupa la division doble// la fprmula es se multiplica por 1000 para obtener mas numeros despues del decimal
#y n0 se multiplica por 100 se multiplica por 1000 se divide por 10
diferencia_con_max = 100 - curso_de_dalto *1000 // otros_cursos_max /10 
diferencia_con_max = 100 - (curso_de_dalto * 100) / otros_cursos_max
diferencia_con_max = 100 - ((curso_de_dalto * 1000) // otros_cursos_max) / 10
diferencia_con_promedio= 100 - curso_de_dalto/otros_cursos_promedio *100

print(f"el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"el curso de dalto dura un {diferencia_con_promedio}% menos que el promedio")

print("---------------------------------------------------")

#optimizando codigo con redondeo
diferencia_con_min = round(100 - curso_de_dalto / otros_cursos_min * 100, 2)
diferencia_con_max = round(100 - curso_de_dalto / otros_cursos_max * 100, 2)
diferencia_con_promedio= round(100 - curso_de_dalto/otros_cursos_promedio *100, 2)

print(f"el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_con_max}% menos que           el mas lento")
print(f"el curso de dalto dura un {diferencia_con_promedio}% menos que el promedio")        
