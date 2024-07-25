cad1='hola soy Fran'

cad2='bienvenido' 

resultado=cad1.lower()#(minuscula)
# resultado=cad1.upper()(mayuscula)


resultado=cad1.capitalize()#(primera letra mayuscula)

#buscamos una cadena en otra cadena
 
busqueda_find=cad1.find('o')

#buscamos una cadena en otra cadena si no hay conincidencias lanza una excepcion(error)
busqueda_index=cad1.index('a')
#si es numero se deuvelve true
es_num=cad1.isnumeric()

#si es alpha numerico devuelve true

es_alpha=cad1.isalpha()



#cuenta cuantas son las cantidades que coinciden

contar_coincidencias=cad1.count('a')


#cuantas caracteres tiene una cadena

len_caracteres=len(cad1)

#verificamos si una cadena empieza con cierto caracter
empieza_con=cad1.startswith('h')
#verificamos si una cadena termina con cierto caracter
termina_con=cad1.endswith('n')

#remplaza un pedazo de la cadena dada

cadena_nueva=cad1.replace('hola', 'pepe')

#devuelve una matriz(lista)separar cadena

cadena_separada=cad1.split(' ')

print(cadena_separada[0])




