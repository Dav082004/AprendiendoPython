#2 listas, una con nombres y otras con apellidos
nombres = ["Juan","Pedro","Maria","Jose","Luis"]
apellidos = ["Perez","Gomez","Gonzalez","Rodriguez","Fernandez"]

#Registrar esta informacion en un txt de forma optima
with open("resolviendo_problemas\\nombres_y_apellidos.txt","w") as archivo:
    for nombre,apellido in zip(nombres,apellidos):
        archivo.write(f"{nombre} {apellido}\n")