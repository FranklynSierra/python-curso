
lista=["fran",7458,True,1.75]

#tupla no se puede ccambiar los datos
tubla=("fran",7458,True,1.75)
print(lista[0],tubla[1])

lista[3]='walala'

print(lista)

#creando un conjunto (set)

#no puede alterar los datos dentro pero se puede reconstruir,no alamena datos duplicados

conjunto={"fran",7458,True,1.75}
print(conjunto)

#creando un diccionario

diccionario={
    'nombre':'fran',
    'edad':'17',
    'altura':1.71
    
}

print(diccionario['nombre'])