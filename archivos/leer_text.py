
#usando open para abrir un archibo con una codificacion universal utf-8
archivo_sin_leer=open('archivos\\texto.txt',encoding='UTF-8')

#leer archivo completo
# archivo=archivo_sin_leer.read()
#leer linea por lineas
# linea_1=archivo_sin_leer.readlines()


#leer una sola linea

linea=archivo_sin_leer.readline(7)

#cerrar el archivo
archivo_sin_leer.close()

print(linea)