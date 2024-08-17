def sumar_dos():
    while True:
        a=input("Ingrese un número: ")
        b=input("Ingrese otro número: ")
        try:
            resultado = int(a) + int(b)
            
        except:
            print("Error al sumar los números")
        else:
            break
        finally:
            print("Se ejecutó el bloque finally")
    return resultado

        
print(sumar_dos())