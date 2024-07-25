dic={
    'nombre':'fran',
    'apellido':'sierra'
}


print(dic)
#recorriendo diccionario para obetener las claves
for datos in dic.items():
    print(f'la clave es {datos}')


#recorriendo diccionario con item()para obtener la clave y los valores
for datos in dic.items():
    key=datos[0]
    value=datos[1]
    print(f'la clave es {key} el valor es {value}')