

eleccion = "S"
 
ventasTotales = 0 
comisionTotales = 0
tipoVendedor = 0  
comision = 0
tipoComision = 0 
cedula = 0


while eleccion == "S" or eleccion == "s":  

        while True: 
            try: 
                cedula = int(input("Digite la cedula del usuario: "))
                if cedula == "" or cedula <= 0:  
                    print("Cedula invalida, digite numeros positivos o algo.")
                    continue 
                break 
            except ValueError:  
                print("Error. Numero de cedula invalido")

        while True: 
            try: 
                nombre = input("Digite el nombre del vendedor: ")  
                if nombre.isalnum() == False or len(nombre) == 0: 
                    print("Nombre invalido") 
                    continue 
                break 
            except Exception as e : 
                print("Error.   Nombre invalido. \n ", e) 


        print("\n 1.Puerta a Puerta \n 2.Telemercadeo \n 3.Ejecutivo de ventas")


        while True: 
            try:
                tipoVendedor = int(input("\nDigite el tipo de vendedor: "))    
                if tipoVendedor <1 or tipoVendedor >3 or  tipoVendedor == "": 
                    print("Error. Digite numero invalido , digite (1 - 2 - 3) : ") 
                    continue 
                break 
            except ValueError: 
                print("Error. Numero invalido.")


        if tipoVendedor == 1 : 
            tipoComision = 0.20 

        elif tipoVendedor == 2 : 
            tipoComision = 0.15 

        elif tipoVendedor == 3 : 
            tipoComision = 0.25   

        
        
        while True: 
            try:
                ventas = int(input("Digite las ventas del vendedor: ")) 
                if ventas < 0 or ventas == "": 
                    print("Digite un valor positivo y entero.")
                    continue 
                break 
            except ValueError: 
                print("Error. Valor de ventas invalido.")




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

