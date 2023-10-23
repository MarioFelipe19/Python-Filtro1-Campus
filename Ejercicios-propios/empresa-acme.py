def leerId(msj): 
     while True: 
         try: 
             ident = int(input(msj)) 

             if ident < 0 or ident == "": 
                 print("ID incorrecta digite de nuevo") 
                 continue 
             return ident 
         except ValueError: 
             print("Error al ingresar la id...") 
             input("Presione enter para continuar")

def buscarProducto(ident , dicProductos): 
   return ident in dicProductos
        
def leerNombre(msj):  
    while True: 
        try: 
            n = input(msj)  
            n = n.strip()
            if n == "" or not n.isalnum():  
                print("Nombre invalido ..") 
                input("Presione entrer para continuar") 
                continue 
            return n 
        except Exception: 
            print("Error al digitar el nombre")
            input("Presione entrer para continuar")    
     
def leerCant(msj): 
    while True: 
        try: 
            c = int(input(msj)) 
            if c == "" or c <= 0: 
                print("Cantidad invalida digite de nuevo")
                input("Presione enter para continuar") 
                continue 
            return c 
        except ValueError: 
            print("Error al digitar la cantidad")
            input("Presione enter para continuar")

def leerPrecio(msj): 
    while True: 
        try: 
            p = int(input(msj)) 
            if p == "" or p <= 0: 
                print("Precion de producto invalido") 
                input("Presione enter para continuar") 
                continue 
            return p 
        except ValueError: 
            print("Error al ingresar el precio") 
            input("Presione enter para continuar") 

def leerInt(msj): 
    while True: 
        try: 
            op = int(input(msj))
            if op == "" or op < 1 or op > 4: 
                print("Error opcion invalida") 
                input("Presione enter para continuar") 
                continue
            return op 
        except ValueError: 
            print("Error al digitar la opcion") 
            input("Presione enter para continuar")  

def modificarDato(opcion , dicProductos , ident): 
    
    bandera = True

    if opcion == 1:  
        dicProductos[ident]['nombre'] = leerNombre("Nombre ?") 

    elif opcion == 2:  
        dicProductos[ident]['precio'] = leerPrecio("Precio ?") 

    elif opcion == 3:  
        dicProductos[ident]['cantidad'] = leerCant("Cantidad ?")

    elif opcion == 4:  
        bandera = False
        return bandera 
    
    
#SECCION DE IMPRESIONES

def imprimirProductoAgregado(dicProductos , ident): 
    print("\nPRODUCTO AGREGADO".center(40)) 
    print("=" *50) 
    print("Nombre\t\tPrecio\t\tCantidad") 
    print("=" *50) 
    print(f"{dicProductos[ident]['nombre']}\t\t{dicProductos[ident]['precio']}\t\t{dicProductos[ident]['cantidad']}")

def imprimirModificacion(dicProductos , ident):  
    print("\nPRODUCTO MODIFICADO".center(40)) 
    print("=" *50) 
    print("Nombre\t\tPrecio\t\tCantidad") 
    print("=" *50) 
    print(f"{dicProductos[ident]['nombre']}\t\t{dicProductos[ident]['precio']}\t\t{dicProductos[ident]['cantidad']}") 
    input("Presione enter para continuar")
    

def modificarProducto(dicProductos): 

    print("\nModificar producto".center(40))

    ident = leerId("Id? ")  
    existeProducto = buscarProducto(ident , dicProductos)
    if existeProducto == True :  

        print("\nMenu de modificacion") 
        print("1. Nombre")
        print("2. Precio")
        print("3. Cantidad") 
        print("4. Salir")

        opcion = leerInt("Opcion? ") 

        dato = modificarDato(opcion , dicProductos , ident)  

        if dato == True:
            print(imprimirModificacion(dicProductos , ident)) 

        else: 
            return

    else: 
        print("El producto no existe")  
        input("Presione enter para continuar") 
        return

def agregarProducto (dicProductos):   

    print("\n\n*** 1. Agregar empleado\n")

    dicDatos = {} 
    ident = leerId("ID del producto? ") 
    existeProducto = buscarProducto(ident , dicProductos) 
    if existeProducto == True:
        print("La ID ya existe en la lista") 
        return

    dicDatos['nombre'] = leerNombre("Nombre? ") 
    dicDatos['precio'] = leerPrecio("Precio? ") 
    dicDatos['cantidad'] = leerCant("Cantidad? ")

    dicProductos[ident] = dicDatos 

    imprimirProductoAgregado(dicProductos , ident)
    input("Presione enter para volver al menu")

def leerOp(msj):  
    while True: 
        try: 
            n = input(msj)  
            n = n.strip()
            if n == "" or not n.isalnum():  
                print("Nombre invalido ..") 
                input("Presione entrer para continuar") 
                continue 
            return n 
        except Exception: 
            print("Error al digitar el nombre")
            input("Presione entrer para continuar")    
      

def listarProductos(dicProductos):  

    if dicProductos == {}: 
        print("No hay productos agregados") 
        input("Presione enter para continuar")
        return

    print("\n4. Listar productos") 
    contador = 0
    for k , v in dicProductos.items(): 
        print("-" *40) 
        print(f" Codigo: {k} \n Nombre: {v['nombre']} \n Precio $ {v['precio']:,} \n Cantidad: {v['cantidad']:,}") 
        contador += 1  

        if contador % 2 == 0: 
            if leerOp("Desa continuar imprimiendo (s/n)? ") == "s": 
                continue 
            else: 
                return
    print("Ya no hay mas productos ") 
    input("Presion enter para continuar")   


def eliminarProducto(dicProductos): 

    ident = leerId("ID ?") 
    existeProducto = buscarProducto(ident , dicProductos) 

    if existeProducto == False:  
        print("\nEliminar producto")
        print("El id no existe") 
        input("Presione enter para continuar") 
        return 
    
    print(f"El producto {dicProductos[ident]}")
    del dicProductos[ident] 
    print("Ha sido eliminado") 
    input("Presione enter para continuar") 

def ordenarProductos(lst): 
    N = len(lst)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if lst[i][1]["precio"] > lst[j][1]["precio"]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
    return lst


def menu () :  
    while True: 
        try: 
            print("-"*40)
            print("MENU ACME".center(40)) 
            print("-"*40)
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto ")
            print("4. Listar productos")
            print("5. Estrategia de mercadeo")
            print("6. Salir") 

            op = int(input("Opcion (1-6) ?")) 
            if op < 1 or op > 6: 
                print("Error digite de nuevo el numero") 
                input("Presione enter")
                continue 
            return op 
        except ValueError: 
            print("Error al ingresar la opcion...") 
            input("Presione enter") 

dicProductos = {} 

while True: 

    opcion = menu() 

    if opcion == 1: 
        agregarProducto(dicProductos) 

    elif opcion == 2: 
        modificarProducto(dicProductos) 

    elif opcion == 3: 
        eliminarProducto(dicProductos) 

    elif opcion == 4: 
        listarProductos(dicProductos) 

    elif opcion == 5: 
        lstProductos = list(dicProductos.items())
        lstOrdenada = ordenarProductos(lstProductos)  
        print(lstOrdenada)
        

        
    elif opcion == 6:  
        print("Muchas gracias por usar el software Adios")
        input("Presiona enter para salir")
        break 

      
     #Arreglar el none 
     #Saber imprimir la lista ordenada
