frutas= ["manzana", "pera", "uva", "sandia", "melon", "cereza", "fresa", "platano", "naranja", "mandarina"]
numeros = [1,2,3,4,5,6,7,8,9,10]

for fruta in frutas:
    if fruta == "cereza":
        continue
    print(f'Me voy a comer una {fruta}')
    
#Evitar que el bucle termine con un break
for fruta in frutas:
    if fruta == "cereza":
        break
    print(f'Me voy a comer una {fruta}')
else:
    print("El bucle termino")
    
#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)