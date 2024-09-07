import pandas as pd
#usando la funcion read_csv para leer el archivo csv
df=pd.read_csv("archivos\\datos.csv")
df2=pd.read_csv("archivos\\datos.csv")
# df=pd.read_csv("archivos\\datos.csv",names=['names','lastname','age'])

#obteniendo los datos de la columna nombre

# nombres=df['names']
# print(df)

#ordenandfo de forma ascendente
df_ordenado=df.sort_values('edad')

#ordenandfo de forma descendente
df_ordenado_reves=df.sort_values('edad',ascending=False)

#concatenando los 2 caracteres

df_concatenado=pd.concat([df,df2])

#ascendiendo a la primer fila con head()
primer_fila=df.head()

#accediendo las ultimas 3 filas con tail
ultimas_filas=df.tail(3)
#accediendo a la cantidad de filas y columnas con shape

# filas_y_columnas_totales=df.shape
filas_totaltes,columnas_totaltes=df.shape

#obteniendo data estadistica de dataframe:

df_info=df.describe()

#accediendo a un elemento especifico de df con loc
elemento_especifico_loc=df.loc[1,'edad']

#accediendo a un elemento especifico de df con iloc
elemento_especifico_iloc=df.iloc[1,1]

#accediendo todas las filas de una columna
apellidos=df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_1=df.loc[1,:]
#accediendo a la fila 3 con iloc
fila_1=df.iloc[1,:]

#accediendo a filas con edad mayor a 13
mayor_que_13=df.loc[df['edad']>13,:]

print(mayor_que_13)