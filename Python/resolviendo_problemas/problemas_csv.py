import pandas as pd

df = pd.read_csv("resolviendo_problemas\\datos.csv")

#convertir a string los datos de una columna
df['edad']=df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(df['edad'][0])

#reemplazo los datos "asdasdas" por "PQWEQWEQ"
df['nombre'].replace("asdasdas","PQWEQWEQ",inplace=True)