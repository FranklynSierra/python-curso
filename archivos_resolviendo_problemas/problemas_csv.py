
#cambiar el tipo de dato de una columna
import pandas as pd

df=pd.read_csv('archivos_resolviendo_problemas\\datos.csv')
#convertir a string los datos de una columna
df['edad']=df['edad'].astype(str)
#mostrar el tipo de dato el promer elemento de la columna edad

print(df['edad'][0])


#reemplazando el nombre fran ppr franklyn
df['nombre'].replace('fran','franklyn',inplace=True)
print(df['nombre'])

#eliminando las filas con datos faltantes
df=df.dropna()
print(df)

#eliminaod filas repetodas

df=df.drop_duplicates()


#creando un csv con el database resultante (limpio)

df.to_csv('archivos_resolviendo_problemas\\dato.csv')





