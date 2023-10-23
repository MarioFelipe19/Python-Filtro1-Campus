#Agregar e imprimir los nombres de unas listas

lstNombres = [] 

nombre = input("Digite el nombre ")  
lstNombres.append(nombre)  

nombre = input("Digite el nombre ") 
lstNombres.append(nombre)  

for nom in lstNombres:  
    print(f"Nombre: {nom}" )

