
matriculasTotales = 0

eleccion = "S" 

while eleccion == "S" or eleccion == "s":  

    nombre = input("Digite el nombre de usuario: ") 
    codigo = int(input("Digite el codigo: ")) 

    programaAcademico = ""
    becaAcademica = "" 
    indicadorDescuento = 0
    valorPrograma = 0 

    print("\n 1.Tecnico en sistemas \n 2. Tecnico en desarrollo de videojuegos \n 3. Tecnico en animacion digital\n") 

    entradaPrograma = int(input("Seleccione  el numero del programa academico: ")) 

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

    print("\n 1.Beca por rendimiento \ 2. Beca cultural \n") 

    entradaBeca = int(input("Digite el numero de la beca que posee: "))

    if entradaBeca == 1 :  
        becaAcademica = "Beca por rendimiento" 
        indicadorDescuento = 0.5 
    elif entradaBeca == 2 : 
        becaAcademica = "Beca cultural" 
        indicadorDescuento = 0.4 
    else: 
        becaAcademica = "Ninguna" 
        
    valorNetoPrograma = valorPrograma * indicadorDescuento 

    matriculasTotales += valorNetoPrograma

    print("\n" , "=" *40) 

    print(f"Programa academico: {programaAcademico}") 
    print(f"Tipo de descuento: {indicadorDescuento} %") 
    print(f"Valor final de descuento {valorNetoPrograma:,.0f}") 
    print(f"Valor de matriculas totales {matriculasTotales:,.0f}")

    print("\n" , "=" *40) 

    eleccion = input("Desea continuar [S-s]? , sino digite cualquier otra cosa")
