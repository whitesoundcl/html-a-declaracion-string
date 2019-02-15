# Pequeño programa que imprime el contenido de un archivo de texto
# a texto que puede ir dentro de una declaración de String.
# Pensado especificamente para utilizarlo con arduino.

import sys

if len(sys.argv) == 1:
    print("USO: html_ard.py [RUTA Y NOMBRE DEL ARCHIVO]")
    quit()

archivo = open(sys.argv[1])

print(archivo.read().replace("\"", "\\\"").replace("\n", "\\\n"))
