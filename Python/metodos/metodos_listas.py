#Creando una lista con list()
lista = list(["hola","nombre",1231])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista 
agregando_con_append = lista.append("ola")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"jijija")

#agregando varios elementos a la lista
lista.extend([128,"Prueba"])

#eliminando un elemento de la lista (por su indice)
lista.pop(0)
#para eliminar el ultimo valor se usa el -1

#remuviendo un elemento de la lista por su valor
lista.remove(128)

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando con sort, solo funciona con valor numericos y booleans
lista2 = list([192,False,True,121,2321,12321,2131])
lista2.sort()

print(lista2) 