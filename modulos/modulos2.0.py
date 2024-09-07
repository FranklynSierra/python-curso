#si el modulo estuviera dentro de una misma carpeta de la misma ruta
# import funciones_modulo.saludar as m_saludar

import sys
sys.path.append('C:\\Users\\Sierra\\pythoncurso\\funciones_modulo')


import saludar
print(saludar.saludar('ffff'))