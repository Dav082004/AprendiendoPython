#pedir nombre y edad de los compañeros de clase asistentes

def obtener_companeros(cantidad_companeros):
    companeros = []
    for i in range(cantidad_companeros):
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        companero = (nombre, edad)
        companeros.append(companero)
    companeros.sort(key=lambda x: x[1])
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    return asistente, profesor

asistente,profesor = obtener_companeros(5)

print(f"El profe es {profesor} y el asistente es {asistente}")