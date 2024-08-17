import pandas as pd

#usando la funcion read_csv de pandas para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")


#df = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])


#obteniendo los datos de la columnna "Nombre"
nombres=df["nombre"]

#ordenando el dataframe por la edad
df_orde_asc = df.sort_values("edad")

#ordenando el dataframe por la edad de forma descendente
df_orde_desc = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concat = pd.concat([df,df2])

#accediendo  a la primeras 3 filas con head()
primer_fila = df.head(3)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[0,2]

#accediendo a todas los apellidos con loc
apellidos_loc = df.loc[:,"apellido"] 

#accediendo a todas los apellidos con loc
apellidos_iloc = df.iloc[:,1] 

#accediendo a la fila 3 con loc 
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc 
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df[df["edad"]>30,:]



print(mayor_que_30)