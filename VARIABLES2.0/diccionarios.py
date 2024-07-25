#creando diccionarios con dict()

diccionario=dict(nombre='fran',apellido='sierra')
#laas listas no pueden ser claves y usamos frosenset para meter conjuntos

dic={('fran','sierra'):'regrtg'}

#creando diccionarios con fromkeys()con dos parametros y  ccon valor defecto none
dickey2=dic.fromkeys(['nombre','appelidp'])
#creando diccionarios con fromkeys() con dos parametros y añadiendo un valor que es ñam
dickey=dic.fromkeys(['nombre','appelidp'],'ñam')






print(diccionario,dic,dickey)