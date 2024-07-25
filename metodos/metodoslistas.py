#creando una lista con list
lista=list(['hola','fran',45])
#devuelve la cantidad de elelmentos de la lista
resultado=len(lista)
#agregando elemento con append y se modifica directamente a la lista
lista.append('te amo')


"agregando un elemtno a la lista en un indice especifico"

lista.insert(3,'toma')

#agregando varios elementos a la lista
lista.extend(['list',4,False])


#eliminando un elemento de la lista por su indice
lista.pop(0)

#si quieres eliminar el ultimo elemento de la lista se usa -1 y asi sucesvamente

lista.pop(-2)

#removiendo un elemento de la lista por su valor

lista.remove('toma')

#eliminando todos los elementos de la lista

# lista.clear()
lista_sort=([48,877,67,True])
lista_sort.sort()

#invirtiendo los elementos de una lista
lista_sort.reverse()
print(lista,lista_sort)