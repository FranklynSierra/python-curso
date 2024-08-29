#




def alumnos(cantidad):
    compañeros=[]


    for i in range(cantidad):
       nombre=input('ingresa el nombre')
       edad=int(input('edad del compañero'))
       compañero=(nombre,edad) 
       compañeros.append(compañero)  
    compañeros.sort(key=lambda x:x[1])
    asistente=compañeros[0][0]
    profesor=compañeros[-1][0]
    return asistente,profesor

asistente,profesor=alumnos(5)

print(f' el asistente es {asistente}')
print(f' el profesor es {profesor}')

    
