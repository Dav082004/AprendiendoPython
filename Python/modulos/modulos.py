#importando un modulo y asignando el nombre "m_saludar"
#import modulo_saludar as m_saludar
#para importar una funcion fuera de la carpeta usar import sys y colocar la ruta de archivo

from modulo_saludar import saludar

import modulo_saludar

modulo_saludar.saludar("Juan")

print(saludar)