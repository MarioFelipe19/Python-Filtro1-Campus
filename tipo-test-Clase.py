import json

def guardarlibro(lstlibro, ruta):
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar el libro.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    try:
        json.dump(lstlibro, fd)
    except Exception as e:
        print("Error al guardar la información del libro.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    return True


def leerId(msj):
    while True:
        try:
            id = input(msj).lower()
            if id == "":
                print("id Inválido")
                continue
            return id
        except ValueError:
            print("Código no válido.")
            input("Presione cualquier tecla para continuar...")

def existeId(id, lstlibro):
    pos = 0
    for datos in lstlibro:
        k = str(list(datos.keys())[0])
        if k == id:
            return pos
        pos +=1
    return -1


def mnubuscarLibro(lstlibro):
    print("\n\n2. Buscar Libro\n")
    
    id = leerId("Ingrese el id:")

    posLibro = existeId(id, lstlibro) #buscarlibro(lstlibro, id)
    if posLibro == -1:
        print("El Libro con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n", "=" * 30)
    print("Título:", lstlibro[posLibro][id]["Titulo"])
    print("Autor:", lstlibro[posLibro][id]["Autor"])
    print("Precio:", lstlibro[posLibro][id]["Precio"])
    print("\n", "=" * 30)
    input("\n Presione cualquier tecla para volver al menu...")


def modificarLibro(lstlibro):
    print("\n\n3. Modificar Libro\n")
    
    id = leerId("Ingrese el id:")
    posLibro = existeId(id, lstlibro)
    if posLibro == -1:
        print("El Libro con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Título\n2. Autor\n3. Precio\nOpcion?: "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break

    print("\n", "=" * 30)
    if op == 1:
        titulo = input("ingrese el nuevo Titulo:")
        lstlibro[posLibro][id]["Titulo"] = titulo

    elif op == 2:
        #cantHoras = leerHoraTrabEmpl()
        autor = input("ingrese el nuevo Autor: ")
        lstlibro[posLibro][id]["Autor"] = autor
        
    elif op == 3:
        #valHora = leerValHoraEmpl()
        precio = input("ingrese el nuevo Precio: ")
        lstlibro[posLibro][id]["Precio"] = precio
        
  


def agregarlibro(lstlibro, ruta):
    print("\n\n1. Agregar Libro")
    id = leerId("Ingrese el Código: ")
    if not existeId(id, lstlibro):# esto no lo entiendo
        print("--> Ya existe un libro con ese ID")
        input("Presione cualquier tecla para continuar\n")
        id = input("\nIngrese el Código: ")
    
    titulo = input("Título: ")
    autor = input("Autor: ")
    precio = int(input("Precio: "))
    
    diclibro = {}
    diclibro[id] = {"Titulo": titulo, "Autor": autor, "Precio": precio}
    
    lstlibro.append(diclibro)
    
    if guardarlibro(lstlibro, ruta) == True:
        input("El libro ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrió algún error al guardar el libro.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("*** REGISTRO DE LA LIBRERÍA ***".center(40))
            print("MENU".center(40))
            print("1. Agregar")
            print("2. Ver")
            print("3. Editar")
            print("4. Salir")
            op = int(input(">>> Opción (1-4)? "))
            
            if op < 1 or op > 4:
                print("Opción no válida. Escoja de 1 a 4.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 4.")
            input("Presione cualquier tecla para continuar...")

def cargarInfo(lstlibro, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstlibro = json.load(fd)
        else:
            lstlibro = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstlibro

# PROGRAMA PRINCIPAL
rutaFile = "Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\datlibros.json" 
lstlibro = []
lstlibro = cargarInfo(lstlibro, rutaFile)
while True:
    op = menu()

    if op == 1:
        agregarlibro(lstlibro, rutaFile)
    elif op == 2:
        mnubuscarLibro(lstlibro)

    elif op == 3:
        modificarLibro(lstlibro)
       
    else:
        # Salir
        print("\nGracias por usar el programa")
        break