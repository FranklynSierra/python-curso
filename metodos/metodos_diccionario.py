dic={
    "fran":'sierra',
    "edad":'17',
    "meta":'cocina'
}
#nos devuelve un objeto dict_item
claves1=dic.keys()


#obtenriendo un elemento con get y si produce un dato incorrecto , el programa sigue
claves=dic.get('fran')

#eliminando todo el diccionario
# claves2=dic.clear()

#eliminando un elemento del diccionario
claves=dic.pop('fran')

#obteniendo un elemento dict_items iterable

dic_iterable=dic.items()

print(dic_iterable)