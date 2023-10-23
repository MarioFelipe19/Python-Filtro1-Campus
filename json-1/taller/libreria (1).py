import json

def guardarLibro(lstLibreria , ruta): 
    
    try: 
        fd = open(ruta , "w") 
    except Exception as e: 
        print("Error al abrir el archivo para guardar el el libro\n" , e) 
        return None
    
    try: 
        json.dump(lstLibreria, fd) #Carga el archivo
    except Exception as e: 
        print("Error al guardar la informacion del libro\n" , e)
        return None

    fd.close() 
    return True


def leerId(msj): 
    while True: 
        try:  
            id = str(input(msj))   
            if id == "" : 
                print("Id invalido")
                continue
            return id
        except ValueError:
            print("Id no válida.")
            input("Presione cualquier tecla para continuar...") 

def existeId(id , lstLibreria): 
    for datos in lstLibreria:  
        k = list(datos.keys())[0]  #Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente
        if k == id:
            return True 
    return False

def cargarInfo(lstLibreria , ruta): 
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

def agregarLibro(lstLibreria, rutaFile): 
    print("\n\n1.Insertar Libro") 

    id = leerId("Id del libro: " )

    while existeId(id , lstLibreria):  
        print("-> Ya existe un libro con esa id") 
        input() 
        id = int(input("\nIngrese el ID: "))  

    titulo = input("Nombre") 
    autor = input("Autor")
    precio = int(input("Precio"))

    dicLibros = {}
    dicLibros[id] = {"titulo":titulo , "autor":autor , "precio":precio } 

    lstLibreria.append(dicLibros)

    if guardarLibro(lstLibreria , rutaFile)  == True:

        input("El libro ha sido agregado con exito") 
    
    else: 
        input("Ocurrio algun error al guardar el empleado")
   
def consultarLibro(lstLibreria):  
    id = leerId("Id")  
    if not existeId(id , lstLibreria): 
        print("La id no existe")
        return
    
    for i in range(len(lstLibreria)): 
        datos = lstLibreria[i]
        k = list(datos.keys())[0] 
        if k == id: 
            for elemento in lstLibreria[i]: 
                print(f"Titulo:{lstLibreria[i][elemento]['titulo']}")
                print(f"Autor:{lstLibreria[i][elemento]['autor']}")
                print(f"Precio:{lstLibreria[i][elemento]['precio']}") 
                input("Enter para contuniar")

def editarLibro(lstLibreria, rutaFile):  
    fd = open(rutaFile , "w")

    print("\n\n3.Modificar empleado") 
    id = int(input("Ingrese el ID: ")) 

    if  existeId(id , lstLibreria) == True: 
        
        op = int(input("\n1. Nombre\n2. Autor\n3.Precio "))

        for i in range(len(lstLibreria)):  
            datos = lstLibreria[i] 
            k = list(datos.keys())[0]
            if k == id:  
                for d in lstLibreria[i]:
                    
                    if op == 1: 
                        nombre = input("Nombre? ") 
                        lstLibreria[i][d]["nombre"] = nombre 

                    elif op == 2: 
                        edad = input("Autor? ")
                        lstLibreria[i][d]["autor"] = edad 

                    elif op == 3: 
                        sexo = input("Precio? ")
                        lstLibreria[i][d]["precio"] = sexo   

    else: 
        print("El id no existe")                
                
    json.dump(lstLibreria, fd) 
    fd.close()



def menu():
    while True:
        try:
            print("*** LIBRERIA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Insertar libro ")
            print("2. Consultar libro ") 
            print("3. Editar informacion") 
            print("4. Borrar libro") 
            print("5. Listar por nombre")
            print("6. Listar por autor")
            print("7. Listar por precio")
            print("8. Salir")
            
            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...") 

rutaFile = "json-1/taller/datLibreria.json" 
lstLibreria = []
lstLibreria = cargarInfo(lstLibreria, rutaFile)   


while True:

    op = menu()

    if op == 1:
        agregarLibro(lstLibreria, rutaFile)
    elif op == 2:
        consultarLibro(lstLibreria) 
    elif op == 3:
        editarLibro(lstLibreria , rutaFile)
    elif op == 4:

        consultarLibro(lstLibreria)
    elif op == 5:
        
        consultarLibro(lstLibreria)
    elif op == 6:
        
        consultarLibro(lstLibreria) 
    elif op == 7:
        
        consultarLibro(lstLibreria)
    elif op == 8:
        print("Gracias por usar la libreria digital")
        input("Presion enter para salir")
        break

