def agregarEmpleado():  

    print("\n1. DATOS EMPLEADO") 
    datEmpleado = {} 
    datEmpleado["codigo"]= leerIdent("Codigo? ") 
    datEmpleado["nombre"] = leerNombre("Nombre? ")
    datEmpleado["horas"] =  leerHoras("Horas trabajadas (1-160) ? ")
    datEmpleado["valHoras"] = leerValorHoras("Valor hora (8.000 - 150.000)") 
    datEmpleado['nomina'] = datEmpleado['horas'] * datEmpleado["valHoras"]
    
    lstEmpleados.append(datEmpleado) 


def leerIdent(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 1 or num == "":
                print("Numero invalido digite de nuevo")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...")

def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip("")
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e) 

def leerHoras(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0 or num > 160 or num == "":
                print("Numero de horas inválido.")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...")  

def leerValorHoras(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 0 or num < 8000 or num > 150000 or num == "":
                print("Valor inválido. Debe estar en el rango de 8.000 a 150.000")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...") 

def buscarEmpleado(lstEmpleados , idEmpl):
    for i in range(len(lstEmpleados)): 
        if(lstEmpleados[i]["codigo"] == idEmpl): 
            return i 
    return -1

def eliminarEmpleado(pos):  
    lstEmpleados.remove(lstEmpleados[pos]) 
    print("El empleado ha sido eliminado")

def modificarEmpleado(lstEmpleados): 
    print("\n\n2. Modificar Empleado\n") 
    idEmpl = leerIdent("Codigo?") 
    posEmpl = buscarEmpleado(lstEmpleados , idEmpl) 
    if posEmpl == -1:
        print("El código del empleado no existe.")
        input()
        return 

    print("\n") 
    while True:
        try:
            op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
            if op < 1 or op > 3:
                print("Opción inválida")
                input()
                continue
            break 
        except ValueError: 
            print("Error al digitar la opcion...")

    
    if op == 1: 
        nombre = leerNombre("Nombre?") 
        lstEmpleados[posEmpl]["nombre"] = nombre 

    elif op == 2: 
        cantHoras = leerHoras("Horas?") 
        lstEmpleados[posEmpl["horas"]] = cantHoras 

    elif op == 3: 
        valHora = leerValorHoras("Valor horas?")
        lstEmpleados[posEmpl]["valHoras"] = valHora  

        

def imprimirEmpleados(lst): 

   for i in range(len(lst)): 
        print(f"Nombre: {lst[i]['nombre']}\n Id: {lst[i]['codigo']}\n Horas: {lst[i]['horas']}\n Valor por hora: {lst[i]['valHoras']}") 


def datosNomina(): 
    empleID = leerIdent("Id?")
    posEmple = buscarEmpleado(lstEmpleados , empleID)  
    if posEmple == -1: 
        print("La id no existe") 
        return
    nomina = calcularNomina(posEmple) 
    return nomina

def nominaBruto(salarioBruto): 
     
    if salarioBruto < 1160000: 
        salarioBruto + 140600 
    return salarioBruto 

def nominaNeto(bruto):   
    eps = bruto * 0.04 
    pension = bruto * 0.04  
    nomina = bruto - (eps + pension) 
    return nomina


def calcularNomina(posicion):  
    salario = lstEmpleados[posicion]['nomina']

    bruto = nominaBruto(salario)
    nomina = nominaNeto(bruto)   
    

    print(f"Nombre: {lstEmpleados [posicion] ['nombre']} ")
    print(f"La nomina es {nomina:,}")

def imprimirEmpleadosNomina(lst):  
     
     for i in range(len(lst)):
        print(f"Nombre: {lst[i]['nombre']}\n Id: {lst[i]['codigo']}\n Horas: {lst[i]['horas']}\n Valor por hora: {lst[i]['valHoras']}\nNomina: ${lst[i]['nomina']:,}") 
    

def menu ():  
    while True: 
        try: 
            print("\n*****NOMINA ACME MENU******")  
            print("1. Agreagar un empleado") 
            print("2. Modificar empleado") 
            print("3. Buscar empleado") 
            print("4. Eliminar empleado") 
            print("5. Lista de empleados") 
            print("6. Listar nomina de un empleado") 
            print("7. Listar nomina de todos los empleados") 
            print("8. Salir") 
            op = int(input(">>>>>> Opcion (1-8): ")) 
            if op <1 or op > 8: 
                print("Opcion no valida. Escoja de 1 a 8. ")  
                input("Presione cualquier tecla para continuar: ")
                continue 
            return op #Devulve el valor op 
        except ValueError:  
            print("Opcion no valida. Escoja de (1-8 )") 
            input("Presione cualquier tecla para continuar: ")  

lstEmpleados = []

while True:  

    opcion = menu() 

    if opcion == 1:  
        agregarEmpleado()
        print("Empleado agregado con exito")
        
    if opcion == 2:  
        modificarEmpleado(lstEmpleados) 
        

    if opcion == 3:  
        identificacion = leerIdent("Id ?") 
        posicionEmple = buscarEmpleado(lstEmpleados , identificacion)   
        if posicionEmple == -1: 
            print("El empleado no existe") 
        else: 
            print(lstEmpleados[posicionEmple]) 

    if opcion == 4: 
        identificacion = leerIdent("Id? ")    
        eliminarEmpleado(buscarEmpleado(lstEmpleados , identificacion))

    if opcion == 5:  
          
        imprimirEmpleados(lstEmpleados) 

    if opcion == 6:  

        datosNomina()

    if opcion == 7: 

        imprimirEmpleadosNomina(lstEmpleados) 

    if opcion == 8:
        print("Muchas gracias por usar el software")
        break        

        
