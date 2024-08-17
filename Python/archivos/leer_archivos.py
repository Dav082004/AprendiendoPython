#archivo = open("archivos\\pruebatexto.txt",encoding="utf-8")
#leer archivo completo
#archivo=archivo_sin_leer.read()

#leer una sola linea
#linea = archivo.readline()

#leer linea por linea
#lineas=archivo_sin_leer.readlines()

#cerrando el archivo
#archivo.close()

#print(archivo.read())

#abriendo correctamente el archivo,mas rapido,menos recursos
with open("archivos\\pruebatexto.txt",encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(archivo.read())
    
