fd = open("Persistencia-datos-13/mbox-short.txt" , "r") 

cd = 0
cp = 0

for linea in fd: 
    linea = linea.strip() #Contar las lineas o renglones
    cp += len(linea.split(" ")) #Contar las palabras

    """for lin in linea.split(" "): 
        if lin.isalnum(): 
            cp += 1"""
    cd += 1 



fd.close() 

print("La cantidad de lineas son: " , cd)
print("La cantidad de palabras es: " , cp)