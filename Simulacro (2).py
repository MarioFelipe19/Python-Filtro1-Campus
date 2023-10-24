def leerIDprod():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")

def leerNombreprod():
    while True:
        try:
            nom = input("Ingrese el nombre del producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerPrecio():
    while True:
        try:
            n = int(input("Ingrese el precio del producto: "))
            if n <= 0 :
                print("Valor del producto debe ser positvo o mayor a Cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el precio del producto")

def leerCantidad():
    while True:
        try:
            n = int(input("Ingrese la catidad del producto: "))
            if n <= 0 :
                print("la catidad debe ser mayor a 0 o numero positivo")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def buscarProducto(dicProductos, idProd):
 
    return idProd in dicProductos


def agregarproducto(dicProductos):
    print("\n\n*** 1. Agregar producto\n")
    dicDatos = {}
    id = leerIDprod()
    if buscarProducto(dicProductos, id) == True:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatos["nombre"] = leerNombreprod()
    dicDatos["Precio"] = leerPrecio()
    dicDatos["Cantidad"] = leerCantidad()
  
    
    dicProductos[id] = dicDatos

    print("\n Producto Agregado")
    input("\n Presione cualquier tecla para volver al menu...")

def modificarproducto(dicProductos):
    print("\n\n2. Modificar Producto\n")
    
    idPro = leerIDprod()
    existPro = buscarProducto(dicProductos, idPro)
    if existPro == False:
        print("El código del producto no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Precio\n3. Cantidad\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreprod()
        dicProductos[idPro]["nombre"] = nombre
    elif op == 2:
        Precio = leerPrecio()
        dicProductos[idPro]["Precio"] = Precio
        
    elif op == 3:
        Cantidad = leerCantidad()
        dicProductos[idPro]["Cantidad"] = Cantidad

    print("\n Producto Modificado")
    input("\n Presione cualquier tecla para volver al menu...")

def eliminarprodcuto(dicProductos):
    print("\n\n3. Eliminar Producto\n")
    
    idPro = leerIDprod()
    existPro = buscarProducto(dicProductos, idPro)
    if existPro == False:
        print("El producto con ese código no ha sido ingresado.")
        input()
        return
    del(dicProductos[idPro])
    
    print("El Producto  fue eleiminado.")
    input("\n Presione cualquier tecla para volver al menu...")
    return
        
   
def Listarvariosproductos(dicProductos):
    print("\n\n4. Listar Producto\n")
 
    print("\n", "=" * 30)
    
    for k, v in dicProductos.items():
        print(f'ID del Producto: {k}\t\t\nNombre del prodcuto: {v["nombre"]}\t\t\nPrecio del producto : {v["Precio"]}\t\t\nCantidad del producto : {v["Cantidad"]}')
        
    print("\n", "=" * 30)  
    input("\n Presione cualquier tecla para volver al menu...")      

    
    

def menu():
    while True:
        try:
            print("*** PRODUCTOS ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar varios productos")
            print("5. Estrategia de mercadeo")
            print("6. Salir")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")


dicProductos= {}
while True:
    op = menu()
    if op == 1:
        agregarproducto(dicProductos)
      
    elif op == 2:
        modificarproducto(dicProductos)
    
    elif op == 3:
        eliminarprodcuto(dicProductos)
    elif op == 4:
        Listarvariosproductos(dicProductos)
    elif op == 5:
        print("\n\nEsta opcion aun no esta disponible, vuelva a preguntar el lunes para mayor informacion XD")
        input("Presione cualquier tecla para continuar...")
    elif op == 6:
        print("\n\nGracias por usar el software. Adios")
        break