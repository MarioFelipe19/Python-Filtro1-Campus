"""
fd = open("Persistencia-datos-13/datos-empleados.txt" , "r") 



lstDatos = [] 


for linea in fd:
    lstDatos.append(linea.split(","))
   
for f in range(1, len(lstDatos)): 
    for k in range(len(lstDatos[0])): 
            print(lstDatos[0][k].strip(),end=": ") 
            print(lstDatos[f][k].strip())
             
        


fd.close() 
""" 

fd = open("Persistencia-datos-13/datos-empleados.txt" , "r") 


for linea in fd: 
    if linea.strip() !="" and not linea.startswith("ID"): 
        datos = linea.split(",")
        print(f"ID:{datos[0]}\nNOMBRE:{datos[1]}\nEDAD:{datos[2]}\nSEXO:{datos[3]}\nCELULAR:{datos[4].strip()}") 
        
        print("="*30)

fd.close()