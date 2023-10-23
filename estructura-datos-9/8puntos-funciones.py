
def leerHoraTraba(): 
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.") 

def leerValHora(): 
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.") 

def leerNombreEmpl(): 
    while True:
        try:
            nom = input("Ingrese el nombre del empleado:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerIDEmpl(): 
    while True: 
        try: 
            n = int(input("Ingrese el id del empleado")) 
            if n < 1 or n == "": 
                print("ID invalido , Debe ser mayor a cero") 
                continue 
            return n 
        except ValueError: 
            print("Error al ingresar el ID")

def buscarEmpleado(lstEmpleado , idEmpl):
    for i in range(len(lstEmpleado)): 
        if(lstEmpleado[i][0] == idEmpl): 
            return i 
    return -1

def imprimirEmple(emple): 
    if emple == -1: 
        print("El empleado no existe") 
    return emple

def agregarEmpleado(lstEmpleado):  
    print("\n\n***1. Agregar empleado\n") 
    lstDatos = [] 
    id = leerIDEmpl() 
    if buscarEmpleado(lstEmpleado, id) != -1: 
        print("El id ya existe en la lista") 
        input()
        return
    lstDatos.append(id) 
    lstDatos.append(leerNombreEmpl())
    lstDatos.append(leerHoraTraba())
    lstDatos.append(leerValHora()) 

    lstEmpleado.append(lstDatos)

def modificarEmpleado(lstEmpleado): 
    print("\n\n2. Modificar Empleado\n") 
    idEmpl = leerIDEmpl() 
    posEmpl = buscarEmpleado(lstEmpleado , idEmpl) 
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
        nombre = leerNombreEmpl() 
        lstEmpleado[posEmpl][0] = nombre 

    elif op == 2: 
        cantHoras = leerHoraTraba() 
        lstEmpleado[posEmpl[0]] = cantHoras 

    elif op == 3: 
        valHora = leerValHora()
        lstEmpleado[posEmpl][0] = valHora

def eliminarEmpleado(pos):  
    lstEmpleado.remove(lstEmpleado[pos]) 
    print("El empleado ha sido eliminado")

def listarEmpleados(lst):  
    for i in range(len(lst)): 
        print(f"Nombre: {lst[i][1]}\n Id: {lst[i][0]}\n Horas: {lst[i][2]}\n Valor por hora: {lst[i][3]}") 

def datosNomina(): 
    empleID = leerIDEmpl()
    posEmple = buscarEmpleado(lstEmpleado , empleID)  
    if posEmple == -1: 
        print("La id no existe") 
        return
    nomina = calcularNomina(posEmple)

def nominaBruto(horas , valHoras): 
    nomina = horas * valHoras 

    if nomina < 1160000: 
        nomina + 140600 
    return nomina 

def nominaNeto(bruto):   
    eps = bruto * 0.04 
    pension = bruto * 0.04  
    nomina = bruto - (eps + pension) 
    return nomina


def calcularNomina(posicion): 
    horas = lstEmpleado[posicion][2] 
    valHoras = lstEmpleado[posicion][3] 

    bruto = nominaBruto(horas , valHoras)
    nomina = nominaNeto(bruto) 
    print(f"La nomina es {nomina:,}")




  



def menu(): 
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado")
            print("2. Modificar empleado")
            print("3. Buscar emplado")
            print("4. Eliminar empleado")
            print("5. Listar empleados")
            print("6. Listar nómina de un empleado")
            print("7. Listar nómina de todos los empleados")
            print("8. Salir")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...") 

#Programa principal  
lstEmpleado = []
while True: 
    op = menu() 
    if op == 1: 
        agregarEmpleado(lstEmpleado)  
        print(lstEmpleado) 
        input()
    if op == 2: 
        modificarEmpleado(lstEmpleado)
        
    if op == 3:  
        id = leerIDEmpl()
        emple = buscarEmpleado(lstEmpleado , id)
        if emple == -1: 
            print("El empleado no existe ")   
        
        else: 
            print(lstEmpleado[emple])

    if op == 4: 
        id = leerIDEmpl() 
        emple = buscarEmpleado(lstEmpleado , id) 
        eliminarEmpleado(emple)

    if op == 5: 
        listarEmpleados(lstEmpleado)

    if op == 6: 
        datosNomina()
        
    if op == 7: 
        pass
    if op == 8: 
        print("\n\nGracias por usar el software. Adios")
        break 

    