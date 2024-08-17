diccionario={
    "nombre" :"dalar",
    "numero" : "didiqdq",
    "dqwidqd" : 3131,
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#devuelve en consola el dato que esta guardado 
claves =diccionario.get("nombre")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.item()

print(diccionario)