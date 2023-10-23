def leerIDEmpl ():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")

def buscarProducto(dicProductos , id ): 
    return id in dicProductos

def leerNombreProducto(): 
     while True:
        try:
            nom = input("Ingrese el nombre del producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre del producto.", e)
 
def leerPrecioProducto (): 
    while True:
        try:
            n = int(input("Ingrese el precio del producto "))
            if n <= 0 :
                print("Precio invalido")
                continue
            return n
        except ValueError:
            print("Error al ingresar el precio.") 

def leerCantProducto (): 
    while True:
        try:
            n = int(input("Ingrese la cantidad del producto "))
            if n < 0 :
                print("Cantidad invalida...")
                continue
            return n
        except ValueError:
            print("Error al ingresar la cantidad.")

def agregarProducto(dicProductos):  
    print("\n\n*** 1. Agregar producto\n")
    dicDatos = {}  
    id = leerIDEmpl() 
    if buscarProducto(dicProductos, id) == True:
        print("El id ya existe en la lista de los productos")
        input()
        return 
    
    dicDatos["nombre"]  = leerNombreProducto() 
    dicDatos['precio'] = leerPrecioProducto() 
    dicDatos["cantidad"] = leerCantProducto()  

    

    dicProductos[id] = dicDatos 
    print(dicProductos)

def modificarProducto(dicProductos):  
    print("\n\n2. Modificar Producto\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarProducto(dicProductos, idEmpl)
    if existEmpl == False:
        print("El código del producto no existe.")
        input()
        return
    
    print("\n")
    while True: 
        try: 
            op = int(input("\n1. Nombre \n2. Precio \n3. Cantidad \nOpcion? "))
            if op < 1 or op > 3:
                print("Opción inválida")
                input()
                continue
            break  
        except ValueError:
            print("Opción inválida")
            input()
            continue

    if op == 1:
        nombre = leerNombreProducto()
        dicProductos[idEmpl]["nombre"] = nombre

    elif op == 2:
        cantHoras = leerPrecioProducto()
        dicProductos[idEmpl]["precio"] = cantHoras
        
    elif op == 3:
        valHora = leerCantProducto()
        dicProductos[idEmpl]["cantidad"] = valHora


#De mayor a menor segun el precio sin importar cuantos  productos sean


def eliminarProducto(dicProductos):  

    idEmpl = leerIDEmpl() 
    existEmpl = buscarProducto(dicProductos , idEmpl)
    if existEmpl == False:
        print("El código del empleado no existe.")
        input()
        return  
    
    print(f"El producto: {dicProductos[idEmpl]}")
    del dicProductos[idEmpl] 
    print("Fue eliminado") 
    input("Digite una tecla para continuar")

    
def estrategia(dicProductos ): 
    print("\n\n5. Estrategia Comercial\n")   

    for k , v in dicProductos.items(): 
        
        ordenado = sorted(list( dicProductos[k], [v]))
        print(ordenado)
        input() 

        """  for k , v in dicProductos.items():
     
        valores_ord = {k: v for k, v in sorted([k][v].items())}  
        print(valores_ord) """ 
    
  

def listaProductos(dicProductos):  
    for k , v in dicProductos.items(): 
        print(f"Nombre: {v['nombre']} \n Precio $ {v['precio']:,} \n Cantidad: {v['cantidad']:,}")
        input() 
    
#MENU DE PRINCIPAL

def menu():
    while True:
        try:
            print("=" * 30)
            print("PRODUCTOS ACME".center(40)) 
            print("=" * 30)
            print("1. Agregar Producto")
            print("2. Modificar Producto")
            print("3. Eliminar Producto") 
            print("4. Listar productos")
            print("5. Estrategia Comercial")
            print("6. Salir")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...") 


## PROGRAMA PRINCIPAL
dicProductos= {}
while True:
    op = menu()
    if op == 1:
        agregarProducto(dicProductos)
        # print(dicEmpleados)
        # input()
    elif op == 2:
        modificarProducto(dicProductos)
        # print(dicEmpleados)
        # input()
    elif op == 3:
        eliminarProducto(dicProductos)

    elif op == 4:
        listaProductos(dicProductos)   

    elif op == 5: 
        print("Esta opcion no sirve")  
        input()

    elif op == 6: 
        print("\n\nGracias por usar el software. Adios")
        break
