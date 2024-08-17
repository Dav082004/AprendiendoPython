import re

text = '''hola, este es mi cadena 1, 
            como estas, esta es mi cadena 2 y 
            esta es mi cadena 3 y 
            esta es mi cadena 4'''

#haciendo una busca simple
#resultado = re.search("hola",text)

#\d --> busca digitos numericos del 0-9
#resultado= re.findall(r"\d",text)

#\s -> busca espacios en blanco, espacios,tabs,saltos de line
#resutlado = re.findall(r"\s",text)

#\S -> busca cualquier cosa que no sea un espacio en blanco
#resultado = re.findall(r"\S",text)

#. -> busca cualquier cosa excepto un salto de linea
#resultado = re.findall(r".",text)

#\n -> busca saltos de linea
#resultado = re.findall(r"\n",text)

#\ -> cancela el caracter especial,cancelando la funcion del punto y buscando puntos
#resultado = re.findall(r"\.",text)

#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r"\d\.\s",text)

#^ -> busca el inicio de una cadena,busca la palabra hola al inicio de la cadena
#flags=re.M -> busca en todas las lineas
#resultado = re.findall(r"^esta",text,flags=re.M)

#$ -> busca el final de una cadena,busca la palabra 4 al final de la cadena
#flags=re.M -> busca en todas las lineas
#resultado = re.findall(r",$",text,flags=re.M)

#{n} -> busca la cantidad de veces que se repite un caracter

#{n,m} -> busca la cantidad de veces que se repite un caracter en un rango
#resultado = re.findall(r"\d{1,2}",text)

#| -> busca una palabra o la otra
resultado = re.findall(r"cadena 1|cadena 2",text)


    
print(resultado)