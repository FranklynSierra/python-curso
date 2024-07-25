# numero =int(input('dame un numero'))

# resultado =float(numero)/1.3
# print(resultado)

#cantidad de los promedios de otros cursos
cantidad_max=7
cantidad__promedio=4
cantidad_min=2.5

curso=1.5
#primero se divide, luego se multipllica y luego se resta para sacar el porcentaje al parecer
procentaje_max=100-((curso/cantidad_max)*100)
procentaje_min=100-((curso/cantidad_min)*100)
#explicacion o codigo del curso de dalto
procentaje_promedio=100-curso*1000//cantidad__promedio/10
print(round(procentaje_max))
print(round(procentaje_min))
print(procentaje_promedio)

#mostrando las diferencias que hau de un curso con el promedio(dalto)
material_inservible_promedio=5
material_curso=3.5

promedio_inservible=100-cantidad__promedio*1000//material_inservible_promedio/10
promedio_curso=100-curso*1000//material_curso/10


print(promedio_inservible)
print(promedio_curso)


#si vemos 10 horas de este curso, cuanta seria la cantidad de otros cursos

nueva_cantidad_curso=10

promedio_cantidad=round(cantidad__promedio/curso*10)
promedio_otros=curso*100//cantidad__promedio/10
print(promedio_cantidad)
print(promedio_otros)
