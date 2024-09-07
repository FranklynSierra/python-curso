
with open('archivos\\texto.txt','a',encoding='UTF-8') as archivo:
   #agregando el archivo
   
   #usando un bucle para agregar varias lineas
   
    for i in range(5):
        #agregando lineas
        archivo.write(f'linea {i+1} agregada \n')
    
    # x = lambda x: [archivo.write(f' linea {i}') for i in range(x)]
    # print(x)