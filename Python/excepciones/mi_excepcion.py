#craendo mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print("Se ha producido un error: ",err)
#lanzando mi propia excepcion

try:
    raise MiExcepcion("Error de prueba")    
except:
    print("Error controlado")