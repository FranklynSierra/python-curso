#abriendo el arxhivo con with open
with open('archivos\\texto.txt',encoding='UTF-8') as archivo:
    #leyendo el archivo
    contenido=archivo.read()
   #mostramos el archivo
    print(contenido)
#no es necesario cerrarlo al usar with open    