frutas=['banana','pera','manzana','naranja','uva']

#evitando que se coma una naranja con la sentencia continue
for fruta in frutas:
    
    if fruta=='naranja':
        continue
    print(f' me voy a comer una {fruta}')
#evitar que el bucle siga ejecutandose el else tampoco se ejecuta
for fruta in frutas:
    
    if fruta=='pera':
        break
    print(f' me voy a comer una {fruta}')

else: 
   print('bucle terminados')
 


#recorrer una cadena de texto

cadena=' hola como esas'

for letra in cadena:
    print(f'{letra}')




#for en una sola linea de codigo
numeros=[2,3,4,5,6]

#manera tradicional
numeros_duplicados=list()

for numero in numeros:
    numeros_duplicados.append(numero * 2)
  
    
print(numeros_duplicados)  

#con una linea de codigo
numeros_duplicados=[x**500 for x in numeros]

print(numeros_duplicados)