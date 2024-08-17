animales = list(["pez","gato","perro","loro"])
numeros= {31231,21321,1231,12321}

#recorriendo animales
for animal in animales:
    print(animal)

#recorriendo la conjunto de numeros
for numero in numeros:
    resultado= numero - 1
    print(resultado)

#iterando conjuntos del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo la conjunto 1: {numero}")
    print(f"recorriendo la conjunto 2: {animal}")
    
#forma no optima de recorrer una conjunto con su indice
for num in range(len(numeros)):
    print(numeros[num])

#forma optima de recorrer una conjunto con su indice
for num in enumerate(numeros):
    print(num)

#usando else
for numero in numeros:
    print(numero)
else:
    print("el bucle termino")
    
    
    