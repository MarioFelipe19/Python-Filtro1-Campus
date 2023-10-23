def leerIdent(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 1000 or num == "" or num > 10000000000 :
                print("Numero invalido digite de nuevo")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...")  

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

def salarioBruto(horas,valorHora):  

    salarioBruto = horas*valorHora  

    if salarioBruto < 1160000: 
        salarioBruto + 140600 
        return salarioBruto 
    return salarioBruto

def salarioNeto(salarioBruto): 
    eps = salarioBruto * 0.04 
    pension = salarioBruto *0.04 

    salarioNeto = salarioBruto - (eps + pension) 
    return salarioNeto

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
            
lstNombre = [] 
lstId = [] 
lstHoras = [] 
lstValorHora = [] 
lstNominaBruto = [] 
lstNominaNeto = []

while True: 

    opcion = menu()   

    if opcion == 1: 

        print("\n\n1. Agregar un empleado") 
        nombre = leerNombre("Nombre? ")  
        lstNombre.append(nombre)

        ident = leerIdent("Identificacion? ")  
        lstId.append(ident)

        horasTrabajo = leerHoras("Horas trabajadas? (1-160) ") 
        lstHoras.append(horasTrabajo)

        valorHoras = leerValorHoras("Pago por hora? (8.000 - 150.000) ")  
        lstValorHora.append(valorHoras) 

        print("Empleado agregado con exito")  
        input("Presione cualquier tecla para continuar...")
        

    if opcion == 2:  
        print("\n\n2. Modificar empleado")  
        ident = leerIdent("Id ?")  

        if ident in lstId: 
            p = lstId.index(ident) 
            lstNombre[p] = leerNombre("Nuevo nombre? ") 
            lstHoras[p] = leerHoras("Nuevas horas de trabajo? ") 
            lstValorHora[p] = leerValorHoras("Nuevo valor horas? ") 

            print(f"Empleado: {lstNombre[p]} Id: {lstId[p]} Horas: {lstHoras[p]} Valor-hora{lstValorHora[p]}"  )  
            input("Presione cualquier tecla para continuar...")

        else: 
            print("El nombre no existe") 
            input("Presione cualquier tecla para continuar...")

    if opcion == 3: 
        print("\n\n3. Buscar empleado por Id")  
        ident = leerIdent("Id ?")  

        if ident in lstId:    
            p = lstId.index(ident)  
            print(f"Nombre: {lstNombre[p]} Horas: {lstHoras[p]} Valor-hora: {lstValorHora[p]} ")  
            input("Presione cualquier tecla para continuar...") 
        else : 
            print("La id no existe")
            input("Presione cualquier tecla para continuar...")
    
    if opcion == 4: 
        print("\n\n4. Eliminar empleado") 
        ident = leerIdent("Id ? ") 

        if ident in lstId:  
             p = lstId.index(ident)  
             lstNombre.remove(lstNombre[p])
             lstId.remove(lstId[p])
             lstHoras.remove(lstHoras[p]) 
             lstValorHora.remove(lstValorHora[p]) 
             print(f"El usuaro con la id {ident} ha sido eliminado") 
             input("Presione cualquier tecla para continuar...") 
        else: 
            print("La id no existe") 
            input("Presione cualquier tecla para continuar...")


    if opcion == 5: 
        print("\n\n5.Lista de empleados ") 


        for i in range(len(lstNombre)): 
            print(f"Nombre: {lstNombre[i]}\n Id: {lstId[i]}\n Horas: {lstHoras[i]}\n Valor por hora: {lstValorHora[i]}") 
            input("Presione cualquier tecla para continuar...")

    if opcion == 6: 
        print("\n\n6. Listar nomina empleado")  
        ident = leerIdent("Id ? ") 

        if ident in lstId:  
             p = lstId.index(ident) 
             salario = salarioBruto(lstHoras[p] , lstValorHora[p]) 
             print(f"El salario bruto es: {salario:,.0f}")  
             lstNominaBruto.insert(p , salario)

             salarioNuevo = salarioNeto(salario) 
             print(f"El salario neto es: {salarioNuevo:,.0f} ")  
             lstNominaNeto.insert(p , salarioNuevo) 
             input("Presione cualquier tecla para continuar...") 
        else: 
            print("La id no existe") 
            input("Presione cualquier tecla para continuar...")


    if opcion == 7: 
        print("\n\n7. Listar nomina de todos los empleados") 
        for i in range (len(lstNombre)): 
            print(f"Nombre: {lstNombre[i]}\nSalario Neto: {lstNominaBruto[i]}\n SalarioBruto: {lstNominaNeto[i]}") 
            

    if opcion == 8: 
        print("\n\n Muchas gracias por usar el software \n Adios")
        input("Presione cualquier tecla para continuar...") 
        break


            
        
        

       

