import os 
import pathlib
"""file = open("Archivo1.txt", "w" //sirve para crear un archivo) 
file.close()"""
#mostrar el contenido del archivo
"""
with open("Archivo2.txt", "r") as  archivo:
    contenido = archivo.readlines()
print(contenido)"""

"""
with open("Archivo3.txt", "w")as file:
    file.write("lenguajes de programacion :\nPHP\nPyton\nJavascript")
with open("Archivo3.txt", "r")as file:
    texto =file.read()
print(texto)

#para verificar si un archivo existe se debe importar import os e import pathlib  
existe =os.path.isfile("Archivo3.txt")
existe2=os.path.isfile("Archivo4.txt")
print(existe)
print(existe2)
"""
#cambiar el nombre a un archivo
"""
os.rename("Archivo2.txt", "Archivo1.txt")
#eliminar archivos"""
"""
os.remove("Archivo0.txt")"""
#RECORRER EL ARCHIVO PARA COLOCAR ARTICULSO EN UNA LISTA Y LOS PRECIOS EN OTRA }
with open("Archivo2.txt","r") as readfile:
    lineas = readfile.readline()
    articulos = []
    precios = []
    for c_linea in readfile:
        renglon=c_linea.split("#")
        articulos.append(renglon[0])
        precios.append(renglon[1])
print(articulos)
print(precios)