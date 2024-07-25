

animales=['gato','perro','pajaro','cocodrilo']
numeros=[1,2,3,4]
#recorriendo la lista de animales
for animal in animales:
    print(animal)
    
#recorreendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    res=numero*10
    print(res)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print('recorriendo lista 1: ', numero)
    print('recorriendo lista 2: ',animal)
 
#forma no optima de recorrer una lista no funcuona en conjuntod
for numero in range(len(numeros)):
    print(numero)
    
    
    
#forma correcta de recorrer una lista con su indice

for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f'el indice es: {indice} y su valor es {valor}')    
    
tupla=tuple(['franklyn','sierra'])    

for nombre,i in enumerate(tupla):
    
    nombrep=nombre
    apellido=i
    print(f'tu valor es {nombrep} y tu apellido es{apellido}')    






#todo esto funciona igual para las tuplas y conjuntos

#conjuntos es con {} en vez con ()como las tuplas o [] de las listas