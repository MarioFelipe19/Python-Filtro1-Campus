def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

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
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
def buscarEmpleado(dicEmpleados, idEmpl):
    # return dicEmpleados.get(idEmpl) != None
    return idEmpl in dicEmpleados

def mnubuscarEmpleado(dicEmpleados):
    print("\n\n3. Buscar Empleado\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El Empleado con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n", "=" * 30)
    print("Nombre:", dicEmpleados[idEmpl]["nombre"])
    print("Horas trabajadas:", dicEmpleados[idEmpl]["HorasTrabajadas"])
    print("Valor de la hora:", dicEmpleados[idEmpl]["ValorHora"])
    
    input("\n Presione cualquier tecla para volver al menu...")

def modificarEmpleado(dicEmpleados):
    print("\n\n2. Modificar Empleado\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El código del empleado no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        dicEmpleados[idEmpl]["nombre"] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        dicEmpleados[idEmpl]["HorasTrabajadas"] = cantHoras
        
    elif op == 3:
        valHora = leerValHoraEmpl()
        dicEmpleados[idEmpl]["ValorHora"] = valHora
        
    dicEmpleados[idEmpl]["Salario"] = dicEmpleados[idEmpl]["ValorHora"] * dicEmpleados[idEmpl]["HorasTrabajadas"]  

    if dicEmpleados[idEmpl]["Salario"] < 11600000: 
        dicEmpleados[idEmpl]["Salario"] + 140600

    dicEmpleados[idEmpl]["Eps"] = dicEmpleados[idEmpl]["Salario"]*0.04 
    dicEmpleados[idEmpl]["Pension"] = dicEmpleados[idEmpl]["Salario"]*0.04  
    dicEmpleados[idEmpl]['salarioTotal'] = dicEmpleados[idEmpl]["Salario"] - (dicEmpleados[idEmpl]["Eps"] + dicEmpleados[idEmpl]["Pension"])

def listaEmpleados(dicEmpleados): 
    contador = 0
    eleccion = ""
    for k , v in dicEmpleados.items(): 
        print(f"Codigo: {k}\n Nombre: {v['nombre']} \n Horas: {v['HorasTrabajadas']} \n Valor hora: {v['ValorHora']:,}")

        contador += 1  
        mult=1

        if contador == 2 * mult : 
            mult += 1
            eleccion = input("Desea seguir? (s/n)")  
            

            if eleccion.lower() == "n": 
                return
                
        
def agregarEmpleado(dicEmpleados):
    print("\n\n*** 1. Agregar empleado\n")
    dicDatos = {}
    id = leerIDEmpl()
    if buscarEmpleado(dicEmpleados, id) == True:
        print("El id ya existe en la lista")
        input()
        return
    
    dicDatos["nombre"] = leerNombreEmpl()
    dicDatos["HorasTrabajadas"] = leerHoraTrabEmpl()
    dicDatos["ValorHora"] = leerValHoraEmpl()

    dicDatos["Salario"] = dicDatos["ValorHora"] * dicDatos["HorasTrabajadas"] 

    if dicDatos["Salario"] < 11600000: 
        dicDatos["Salario"] + 140600

    dicDatos["Eps"] = dicDatos["Salario"] * 0.04
    dicDatos["Pension"] = dicDatos["Salario"] * 0.04 
    dicDatos["SalarioTotal"] = dicDatos["Salario"] - (dicDatos["Eps"] + dicDatos["Pension"])
    
    dicEmpleados[id] = dicDatos

def eliminarEmpleado(dicEmpleados): 
    print("\n\n2. Eliminar empleado\n")
    
    idEmpl = leerIDEmpl()  
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El código del empleado no existe.")
        input()
        return 
    
    del dicEmpleados[idEmpl]

def listaNomina(dicEmpleados):  
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(dicEmpleados, idEmpl)
    if existEmpl == False:
        print("El código del empleado no existe.")
        input()
        return 
    
    print("\n", "=" * 30)
    print("Nombre:", dicEmpleados[idEmpl]["nombre"])
    print(f"Salario: ${dicEmpleados[idEmpl]['SalarioTotal']:,.2f}")
    input("\n Presione cualquier tecla para volver al menu...")

def listarNominas(dicEmpleados):  
    for k , v in dicEmpleados.items(): 
        print(f"Nombre: {v['nombre']} \n Salario: {v['SalarioTotal']:,}")
        input() 


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

## PROGRAMA PRINCIPAL
dicEmpleados= {}
while True:
    op = menu()
    if op == 1:
        agregarEmpleado(dicEmpleados)
        # print(dicEmpleados)
        # input()
    elif op == 2:
        modificarEmpleado(dicEmpleados)
        # print(dicEmpleados)
        # input()
    elif op == 3:
        mnubuscarEmpleado(dicEmpleados)
    elif op == 4:
        eliminarEmpleado(dicEmpleados)
    elif op == 5:
        listaEmpleados(dicEmpleados)    
    elif op == 6:
        listaNomina(dicEmpleados)    
        
    elif op == 7:
        listarNominas(dicEmpleados)
    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break