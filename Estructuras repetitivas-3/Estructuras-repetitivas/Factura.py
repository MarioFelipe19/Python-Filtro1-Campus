n = int(input("Cuantos usuarios?"))
for i in range (1 , n +1):

    print(f"\n Datos del usuario #{i} ") 
    cod = input("Codigo: ") 
    nom = input("Nombre: ") 
    est = input("Estado [V: Vigente o S: Suspendido]: ") 
    estr = int(input("Estrato [1 al 6]: ") ) 
    con = float(input("Consumo  agua al mes:  [cm3] : ")) 

    #Calcular la tarifa basica
    if est == "V" or est == "v" : 
         
        if estr == 1 : 
            tbas = 10000 
        elif estr == 2 : 
            tbas = 20000 
        elif estr == 3 : 
            tbas = 30000 
        elif estr == 4 : 
            tbas = 45000 
        elif estr == 5 : 
            tbas = 60000 
        elif estr == 6 : 
            tbas = 70000  
        else: 
            tbas = 0
        
    
    #Calcular el valor de consumo
    valcons = con * 200  

    #Valor a pagar 
    valPagar = tbas + valcons

    #Imprimir informe de usuario
    print("\n" , "=" *40) 
    print("\tNombre: " , nom)
    print(f"\tValor tarifa basica: ${tbas:,}") 
    print(f"\tValor de consumo ${valcons:,.0f}") 
    print(f"\fValore de la factura de agua: ${valPagar:,.0f}")
