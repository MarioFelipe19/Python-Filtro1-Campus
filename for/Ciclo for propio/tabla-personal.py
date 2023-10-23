lstPersonas = []  
lstDatos = []

nombre = input("Nombre? ")   
apellido = input("Apellido? ")
id = int(input("Id? "))
tel = int(input("Tel? ")) 

lstDatos.append(nombre)
lstDatos.append(apellido)
lstDatos.append(id)
lstDatos.append(tel)

lstPersonas.append(lstDatos) 
print(lstPersonas)

 

for nom in range(len(lstPersonas)):  
    print(f"\nNombre:{lstPersonas[0][0]}\nApellido: {lstPersonas[0][1]} \nID: {lstPersonas[0][2]}\nTel:{lstPersonas[0][3]} " )
