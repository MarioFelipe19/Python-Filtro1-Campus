matriculasTotales = 0


while True: 
    try: 
        numUsuarios = int(input("Digite el numero de usuarios a matricular: ")) 
        if numUsuarios == "" or numUsuarios < 0: 
            print("El numero de usuarios es incorrecto, digite un numero entero. ") 
            continue 
        break 
    except Exception as e: 
        print("Error al ingresar la cantidad de usuarios: \n " , e)






for i in range(numUsuarios):


    while True: 
        try: 
            nombre = input("Digite el nombre de usuario: ")   
            nombre = nombre.strip()  
            if len(nombre) == 0 or nombre.isalnum() == False: 
                print("Nombre invalido vuelva a digitarlo") 
                continue 
            break 
        except Exception as e: 
            print("Error al ingresar el nombre. \n " , e) 



    while True: 
        try: 
            codigo = str(input("Digite el codigo numerico: "))   
            

            if  len(codigo) == 0 or codigo.isdigit() == False: 
                print("Codigo numerico erroneo ") 
                continue
            break 
        except ValueError: 
            print("Error . Codigo numerico invalido")


    programaAcademico = ""
    becaAcademica = "" 
    indicadorDescuento = 0
    valorPrograma = 0 

    print("\n 1.Tecnico en sistemas \n 2. Tecnico en desarrollo de videojuegos \n 3. Tecnico en animacion digital\n") 

    while True:  
        try: 
            entradaPrograma = int(input("Seleccione  el numero del programa academico: "))

            if entradaPrograma < 1 or entradaPrograma > 3:  

                print("Numero del programa incorrecto , Digite 1 - 2 - 3")
                continue 
            break 
        except ValueError: 
            print("Error. numero de programa invalido")



    if entradaPrograma == 1: 
        programaAcademico = "Tecnico en sistemas" 
        valorPrograma = 800000 

    elif entradaPrograma == 2: 
        programaAcademico = "Tecnico en desarrollo de videojuegos" 
        valorPrograma = 1000000 


    elif entradaPrograma == 3: 
        programaAcademico = "Tecnico en animacion digital"  
        valorPrograma = 1200000 

    print("\n" , "=" *40) 

    print("\n 1.Beca por rendimiento \ 2. Beca cultural \ 3.Ninguna \n ") 


    while True: 
        try: 
            entradaBeca = int(input("Digite el numero de la beca que posee: ")) 

            if entradaBeca <1 or entradaBeca >3: 
                print("Numero de la beca invalido. Digite 1 - 2 - 3") 
                continue 
            break 
        except ValueError: 
            print("Error. Numero de beca invalido.")

    if entradaBeca == 1 :  
        becaAcademica = "Beca por rendimiento" 
        indicadorDescuento = 0.5 

    elif entradaBeca == 2 : 
        becaAcademica = "Beca cultural" 
        indicadorDescuento = 0.4 

    elif entradaBeca == 3: 
        becaAcademica = "Ninguna" 
        indicadorDescuento = 1
        

        
    valorNetoPrograma = valorPrograma * indicadorDescuento 

    matriculasTotales += valorNetoPrograma

    print("\n" , "=" *40) 

    print(f"Programa academico: {programaAcademico}") 
    print(f"Tipo de descuento: {indicadorDescuento} %") 
    print(f"Valor final de descuento {valorNetoPrograma:,.0f}") 
    print(f"Valor de matriculas totales {matriculasTotales:,.0f}")

    print("\n" , "=" *40) 

