animales = list(["pez","gato","perro","loro"])
numeros= list([31231,21321,1231,12321])
#recorriendo animales
for animal in animales:
    print(animal)

#recorriendo la lista de numeros
for numero in numeros:
    resultado= numero - 1
    print(resultado)

#iterando listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo la lista 1: {numero}")
    print(f"recorriendo la lista 2: {animal}")
    
#forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])

#forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    print(num)

#usando else
for numero in numeros:
    print(numero)
else:
    print("el bucle termino")
    
    
    