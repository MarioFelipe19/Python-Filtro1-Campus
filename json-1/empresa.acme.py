import json
def  borrarPersonal(lstPersonal , rutaFile):  
    print("\n\n3.Borrrar Personal") 

    id = int(input("Ingrese el ID: ")) 
    if not existeId(id , lstPersonal):  
        print("No existe un empleado con ese Id") 
        input()
        return

    for i in range(len(lstPersonal)): #Busqueda por posicion
        datos = lstPersonal[i]
        k = int(list(datos.keys())[0]) 
        if k == id: 
            del lstPersonal[i] 
            break 
    
    if guardarEmpleado(lstPersonal , rutaFile) == True: 
        print("El empleado ha sido borrado con exito") 
    else: 
        print("Ocurrio un erro al borrar empleado")

def existeId(id , lstPersonal): 
    for datos in lstPersonal:  
        k = int(list(datos.keys())[0]) #Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente
        if k == id:
            return True 
    return False

def guardarEmpleado(lstPersonal , ruta): 
    
    try: 
        fd = open(ruta , "w") 
    except Exception as e: 
        print("Error al abrir el archivo para guardar el empleado\n" , e) 
        return None
    
    try: 
        json.dump(lstPersonal, fd) #Carga el archivo
    except Exception as e: 
        print("Error al guardar la informacion del empleado\n" , e)
        return None

    fd.close() 
    return True

def agregarPersonal(lstPersonal , ruta): 
    print("\n\n1.Agregar Personal") 

    id = int(input("Ingrese el ID: ")) 

    while  existeId(id , lstPersonal):  
        print("-> Ya existe un empleado con ese ID") 
        input() 
        id = int(input("\nIngrese el ID: "))  

    nombre = input("Nombre") 
    edad = int(input("Edad"))
    sexo = input("Sexo (M/F)")
    telefono = int(input("Telefono: ")) 

    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre , "edad":edad , "sexo":sexo , "telefono":telefono} 

    lstPersonal.append(dicEmpleado) 

    if guardarEmpleado(lstPersonal , ruta)  == True:

        input("El empleado ha sido registrado con exito,\npresione enter para continuar")
    
    else: 
        input("Ocurrio algun error al guardar el empleado")



def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar ")
            print("2. Modificar ")
            print("3. ELiminar ")
            print("4. Vista ")
            print("5. salir ")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

def cargarInfo(lstPersonal , ruta): 
    try: 
        fd = open(ruta, "r") #Fd es la la apertura del archivo
    except Exception as e:  

        try: 
            fd = open(ruta , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": #Si tiene el archivo algo de contenido cargara los datos, sino creara una lista vacia.
            fd.seek(0)
            lstPersonal = json.load(fd) 
        else: 
            lstPersonal = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None 
    
    print(lstPersonal)
    fd.close() #Si se carga todo cierre el archivo
    return lstPersonal #Deculve la lista cargada

def mostrarEmpleado(lstPersonal, rutaFile): 

    print("\n\n4. Buscar empleado") 
    id = int(input("Ingrese el ID: ")) 

    if not existeId(id , lstPersonal): 
        print("El empleado no existe") 
        input()
        return
    
    for i in range(len(lstPersonal)):  
        datos = lstPersonal[i] 
        k = int(list(datos.keys())[0])
        if k == id:
            for d in lstPersonal[i]:
                print(f"Nombre: {lstPersonal[i][d]['nombre']}") 
                print(f"Sexo: {lstPersonal[i][d]['sexo'].upper()}") 
                print(f"Edad: {lstPersonal[i][d]['edad']}") 
                print(f"Tel: {lstPersonal[i][d]['telefono']}") 
                input("")


def modificarEmpleado(lstPersonal, rutaFile):  
    fd = open(rutaFile , "w")

    print("\n\n3.Modificar empleado") 
    id = int(input("Ingrese el ID: ")) 

    if not existeId(id , lstPersonal): 
        print("El empleado no existe") 
        input()
        return  
    
    op = int(input("\n1. Nombre\n2. Edad\n3.Sexo \n4.Tel\nOpcion? "))

    for i in range(len(lstPersonal)):  
        datos = lstPersonal[i] 
        k = int(list(datos.keys())[0])
        if k == id:  
            for d in lstPersonal[i]:

                if op == 1: 
                    nombre = input("Nombre? ") 
                    lstPersonal[i][d]["nombre"] = nombre 

                elif op == 2: 
                    edad = input("Edad? ")
                    lstPersonal[i[d]["edad"]] = edad 

                elif op == 3: 
                    sexo = input("Sexo? ")
                    lstPersonal[i][d]["sexo"] = sexo   
                
                elif op == 4: 
                    tel = input("Tel? ")
                    lstPersonal[i][d]["tel"] = tel 

            json.dump(lstPersonal, fd) 
            fd.close()


## PROGRAMA PRINCIPAL 
rutaFile = "json-1/datPersonal.json"
lstPersonal= []
lstPersonal = cargarInfo(lstPersonal , rutaFile)

while True:

    op = menu()

    if op == 1:
        agregarPersonal(lstPersonal, rutaFile)
    elif op == 2:
        modificarEmpleado(lstPersonal, rutaFile)
    elif op == 3:
        borrarPersonal(lstPersonal , rutaFile)
        
    elif op == 4:
        mostrarEmpleado(lstPersonal, rutaFile)
    elif op == 5:
        print("Gracias por usar el software") 
        break
    