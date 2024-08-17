#creando funcion simple
#def saludar():
#    print("Hola, bienvenido a mi programa")
#    
#saludar()

#creando funcion con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if(sexo == "m"):
        adjetivo = "ola"
    elif(sexo == "f"):
        adjetivo = "olad"
    else:
        adjetivo = "pepe"
        
    print(f"Hola {nombre}, mi {adjetivo} bienvenido a mi programa")
    
saludar("Juan", "m")

#crear una funcion que nos retorne valores
def crear_contra_random(num):
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    num_entero = str(num)
    num= int(num_entero[0])
    c1 = num - 2
    c2 = num - 1
    c3 = num - 6
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña

passq = crear_contra_random(2)
frase = f"Tu contraseña es: {passq}"
print(frase)