numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#creando una funcion lambda
multiplicar_dos = lambda x : x * 2

#creando funcion comun par o no
#def es_par(numero):
#    if (numero % 2 == 0):
#        return True
#usnado filter con una funcion comun
#numeros_pares = filter(es_par, numeros)

#creando lo mismo pero con lambda
numeros_pares = filter(lambda numero: numero % 2 == 0, numeros)

print(list(numeros_pares))


