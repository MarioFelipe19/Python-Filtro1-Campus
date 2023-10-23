archivo = open("Persistencia-datos.py/nombres.txt" , "r") #1ro abrir el archivo por su ubicacion copiar ruta de archivo relativa 2do tipo de apertura

texto = archivo.read() 
print(texto)

archivo.seek(0)#Indico la posicion en donde se coloca el puntero , 0 es el inicio

texto2 = archivo.readline() 
print(texto2)

texto3 = archivo.readlines() #Read lines coloca una lista
print(texto3) 


archivo.close() 