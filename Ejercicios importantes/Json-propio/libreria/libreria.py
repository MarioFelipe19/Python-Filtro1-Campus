#1. Primero abrimos el archivo y lo leemos para poder traer la informacion que tiene  
#2. Sino se puede abrir en lectura abralo en escritura 
#3. Si el archivo tiene algo de contenido se tomara la lista que creamos y se le cargara la informacion del archivo que abrimos "fd"

import json

def cargarInformacion(lst , ruta): 
    try: 
        """1"""
        fd = open(ruta , "r") 

    except Exception as e: 
        print("Error al leer el archivo\n" , e) 

        try: 
           """2"""
           fd = open (ruta , "w") 
        except Exception as d: 
           print("Error al intentar abrir el archivo\n" , d) 
    try:  
        """3"""
        linea = fd.readline() 
        if linea.strip() != "": 
            fd.seek(0) #Se coloca el puntero en la primera posicion 
            lst = json.load(fd) 
        else:  
            lst = [] #Si el archivo esta vacio se crea una lista vacia
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None #Si ocurre un error retorna None 

    fd.close() 
    return lst #Retornamos la lista con los datos

def leerId(msj): # Leer la id como cadena 
    while True: 
        try: 
            id = input(msj)
            if id == "": 
                print("Numero de id invalido") 
                continue 
            return id
        except Exception as e: 
            print("Error al digitar la id\n" , e)

def existeId(lst , id): 
    for datos in lst:  
        k = list(datos.keys())[0] #Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente
        if k == id:
            return True 
    return False

def guardarLibro(lst , ruta): #Traemos la lista que contiene el empleado agregado y la ruta del json

    try:  #Abrimos el json en modo escritura
        fd = open(ruta , "w")  
    except Exception as e: 
        print("Error al abrir el archivo para guardar el libro\n" , e)

    try: #Si abrio guarde la lista de los libros en el archivo
        json.dump(lst,fd)  
    except Exception as e: 
        print("Error al guardar la informacion del empleado\n" , e) 
        return None


    #Si nada fallo entonces cierre el archivo y retorne True
    fd.close() 
    return True
    

def agregarLibro(lstLibreria, ruta):  

    print("\n\n1.Agregar libro")

    id = leerId("Id? ") 

    while existeId(lstLibreria , id): # Si el id existe dentro de la lista lo volvera a pedir
        print("Ya existe un libro con esa Id")
        input("Presione enter para continuar")  
        print("\n\n1.Agregar libro")
        id = input("Id ?")

    #Pido los datos del libro
    nombre = input("Nombre: ")
    autor = input("Autor: ")
    precio = input("Precio: ") 

    #Creo el diccionario donde estara los datos del libro
    dicDatosLibro = {}   

    #Creo la llave y le asigno los datos ingresados 
    #El [id] es que la llave para acceder a un diccionario sera la id que haya insertado el ususario

    dicDatosLibro[id] = {"nombre":nombre , "autor":autor , "precio":precio} 

    #Inserto el diccionario en la lista de la libreria
    lstLibreria.append(dicDatosLibro) 

    #Creamos la funcion guardarLibro para abrir el archivo e insertar la lista con los datos de los libros 

    if guardarLibro (lstLibreria , ruta) == True:  
        #Si nada fallo retorna True y significa que se guardo la listo
        print("El empelado ha sido agregado con exito") 

    else: 
        input("Ocurrio un error al guardar el empleado presione enter para continuar")

                
def consultarLibro(lstLibreria): 


    id = leerId("Id? ") 
    while not existeId(lstLibreria , id): 
        print("La id no existe") 
        return 
    
    #Para recorrer una lista de diccionarios
    for i in range(len(lstLibreria)):  
        datos = lstLibreria[i] 
        k = list(datos.keys())[0]
        if k == id:
            for d in lstLibreria[i]:
                print(f"\nNombre: {lstLibreria[i][d]['nombre']}") 
                print(f"Autor: {lstLibreria[i][d]['autor']}") 
                print(f"Precio: $ {lstLibreria[i][d]['precio']}") 
                input("")

def modificarLibro(lstLibreria, rutaFile):  
    fd = open(rutaFile , "w")

    print("\n\n3.Modificar libro") 
    id = leerId("Ingrese el ID: ") 

    if not existeId(lstLibreria , id): 
        print("El libro no existe") 
        input()
        return  
    
    op = int(input("\n1. Nombre\n2. Autor\n3.Precio \nOpcion? "))

    #Para modificar un diccionario dentro de una lista 
    #Para modificar un dato de un diccionario dentro de una lista 
    
    for i in range(len(lstLibreria)):  
        datos = lstLibreria[i] 
        k = list(datos.keys())[0]
        if k == id:  
            for d in lstLibreria[i]:

                if op == 1: 
                    nombre = input("Nombre? ") 
                    lstLibreria[i][d]["nombre"] = nombre 

                elif op == 2: 
                    autor = input("Autor? ")
                    lstLibreria[i[d]["autor"]] = autor 

                elif op == 3: 
                    precio = input("Precio? ")
                    lstLibreria[i][d]["precio"] = precio   
                
                
    json.dump(lstLibreria, fd) 
    fd.close()
       
        
#MENU PRINCIPAL

def menu (): 
    while True: 
        try: 
            print("\n",lstLibreria)
            print("\nMENU LIBRERIA\n") 
            print("1. Insertar libro")
            print("2. Consultar libro")
            print("3. Modificar libro") 

            op = int(input("Opcion? ")) 
            if op < 1 or op > 3 or op == "": 
                print("Opcion invalida")
                input("Presione enter para continuar")
                continue
            return op 
        except ValueError as e:
            print("Error al validar la opcion\n" , e)
            input("Presione enter para continuar")
             
lstLibreria = [] 
ruta = "Ejercicios importantes\Json-propio\libreria\libreria.json" 
lstLibreria = cargarInformacion(lstLibreria, ruta) 

while True:

    op = menu()

    if op == 1:
        agregarLibro(lstLibreria, ruta)
    elif op == 2:
        consultarLibro(lstLibreria)
       
    elif op == 3:
        modificarLibro(lstLibreria, ruta)
        pass
        