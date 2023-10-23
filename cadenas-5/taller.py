print("Punto 1")

eleccion = "S"
cedula = 0  
ventasTotales = 0 
comisionTotales = 0
tipoVendedor = 0  
comision = 0
tipoComision = 0


while cedula != -1 : 

    if eleccion == "S" or eleccion == "s":
        cedula = int (input("Digite la cedula del vendedor: "))
        nombre = input("Digite el nombre del vendedor: ")  

        print("\n 1.Puerta a Puerta \n 2.Telemercadeo \n 3.Ejecutivo de ventas")

        tipoVendedor = int(input("\nDigite el tipo de vendedor: "))   

        if tipoVendedor == 1 : 
            tipoComision = 0.20 

        elif tipoVendedor == 2 : 
            tipoComision = 0.15 

        elif tipoVendedor == 3 : 
            tipoComision = 0.25  

        ventas = int(input("Digite las ventas del vendedor: ")) 


        comision = ventas * tipoComision


        ventasTotales = ventasTotales + ventas 

        comisionTotales = comisionTotales + comision   

        print("\n" , "=" *30)


        print(f"Ventas:$ {ventas:,.0f}")  
        print(f"Comision por ventas: $ {comision:,.0f}")
        print(f"Ventas totales: $ {ventasTotales:,.0f}")
        print(f"Comisiones totales: $ {comisionTotales:,.0f}")

        print("\n" , "=" *30)
        eleccion = input("Desea continuar? [S-s]") 

print("Muchas gracias")


""" print("Punto 2") 

experto = 0
novato = 0
tipoConductor = 0  
comisionEncomiendas = 0 
comisionPasajes = 0 

comisionExperoPasajesMes = 0
comisionExpertoEncomiendaMes = 0
comisionNovatoPasajesMes = 0
comisionNovatoEncomiendaMes = 0  
totalPago = 0 
eleccion = "S"

while eleccion == "S" or eleccion == "s":

    cedula = int(input("Digite la cedula del conductor : ")) 
    nombre = input("Digite le nombre del conductor: ")


    pasajesMes = int(input("Ventas total de los pasajes mensual: ")) 
    encomiendasMes = int(input("Valor total de las encomiendas mensual: ")) 

    print("\n" , "=" *30)

    print("1.Experto \n2.Novato ")  
    print()
    tipoConductor = int(input("Digite el tipo de conductor: ")) 
    
    if tipoConductor == 1: 

        experto += 1
        comisionPasajesExperto = 0.30   
        comisionEncomiendasExperto = 0.20 

        comisionExperoPasajesMes = pasajesMes * comisionPasajesExperto
        comisionExpertoEncomiendaMes = encomiendasMes * comisionEncomiendasExperto 

        pagoMensual = pasajesMes + comisionExperoPasajesMes + encomiendasMes + comisionExpertoEncomiendaMes



    elif tipoConductor == 2 : 

        novato += 1
        comisionPasejesNovato = 0.20   
        comisionEncomiendasNovato = 0.15 

        comisionNovatoPasajesMes =  pasajesMes * comisionPasejesNovato
        comisionNovatoEncomiendaMes = encomiendasMes * comisionEncomiendasNovato  


        pagoMensual = pasajesMes + encomiendasMes + comisionNovatoPasajesMes + comisionNovatoEncomiendaMes



    totalPago += pagoMensual

    print("\n" , "=" *30)

    print(f"Conductores novatos: {novato}" )  
    print(f"Conductores expertos: {experto}") 
    print(f"Pago total a conductores: {totalPago:,.0f}")  

    eleccion = input("Desea continuar facturando [S-s] sino digite cualquier otro digito: ")

    print("\n" , "=" *30)

print("\n" , "=" *30)
print("Muchas gracias")
 """ 
""" 


print("Punto 3") 

pagoHoras = 0 
cantDocentesA = 0 
cantDocentesB = 0 
cantDocentesC = 0 
pagoMensualAcumulado = 0 
eleccion = "S"


while eleccion == "S" or eleccion == "s":

    documento = input("Digite la cedula del docente: ") 
    nombre = input("Digite el nombre del docente: ")
    categoria = input("Digite la categoria del docente [A-B-C]: ")
    horasTrabajadas = int(input("Digita las horas laboradas al mes: "))  

    print("\n" , "=" *30)



    if categoria == "A" or categoria == "a": 
        pagoHoras = 25000 
        cantDocentesA +=1

    elif categoria == "B" or categoria == "b": 
        pagoHoras = 35000 
        cantDocentesB +=1

    elif categoria == "C" or categoria == "c":
        pagoHoras = 50000  
        cantDocentesC +=1

    pagoMensual = pagoHoras * horasTrabajadas 
    pagoMensualAcumulado += pagoMensual 

    print("\n" , "=" *30)

    print(f"Valor a pagar a {nombre}: $ {pagoMensual:,.0f}\n") 
    print(f"Valor total todos los docentes: $ {pagoMensualAcumulado:,.0f}\n") 
    print(f"Docentes A: {cantDocentesA} \nDocentes B: {cantDocentesB} \nDocentes C: {cantDocentesC}")  

    print("\n" , "=" *30)


    eleccion = input("Desa seguir? [S-s] , sino digite cualquier otra tecla.") 

    print("\n" , "=" *30)

print("Muchas gracias.") """