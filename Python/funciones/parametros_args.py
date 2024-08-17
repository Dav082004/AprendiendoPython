#utilizando args
def suma_total(numeros):
    return sum([*numeros])

    resultado2= suma_total ([5,3,9,2,2,3,54])

#lo mismo pero con args
def suma(nombre, *numeros):
    return f"{nombre}, la suma es de: {sum(numeros)}"

resultado = suma (5,3,9,2,2,3,54)
print(resultado)