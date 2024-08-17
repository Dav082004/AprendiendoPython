cadena1= "ola idqiodq"
cadena2= "ndqdqnwdqwq"

#Convierte todo a mayusculas
resultado = cadena1.upper()

#Minusculas
minus=cadena1.lower()

#El primer char en mayus
primer_mayus= cadena1.capitalize()

#Busca una cadena en otra cadena, la coincidencia que se le pida
coinci= cadena1.find("o")

#buscamos una cadena en otra cadena
busqueda_index= cadena1.index("9")

#Si es numerico nos lanza un true
es_numerico=cadena1.isnumeric()

#Si es alfa numerico, true
es_alfanumerico=cadena1.isalpha()

#buscamos una cadena dentro de otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres que tiene una cadena
contar_caracteres= len(cadena1)

#verficamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("w")

#verficamos si una cadena terminca con otra cadena dada, si es asi devuelve True
termina_con= cadena1.endswith("w")

#reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva= cadena1.replace("la","lu")

#separar cadenas con la cadena que le pasemos
cadena_separada=cadena1.split(",")


print(resultado)