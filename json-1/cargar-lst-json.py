import json 

fd = open("json-1/lista.json" , "r") 


lst = []

lst = json.load(fd) #Cargo el archivo y se asigna a la lista

for e in lst: 
    print(f"Nombre:{e['nombre']}") 
    print(f"Edad:{e['edad']}") 
    print("-" * 30)

fd.close()