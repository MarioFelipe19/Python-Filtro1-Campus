def leerFactorial(msj):  
    while True: 
        try: 
            num = int(input(msj)) 
            if num == "" or num <1: 
                print("Digite un numero entero positivo...") 
                continue 
            return num 
        except ValueError: 
            print("Error, Numero invalido digite nuevamente...") 
            input("Presione cualquier tecla para continuar...")

def factorial(num):  
    numfact = 1
    for i in range(1 , num +1  ): 
        numfact *= i  

    return numfact 
        
def leerHoras (msj): 
     while True: 
        try: 
            num = int(input(msj)) 
            if num == "" or num <1: 
                print("Digite un numero entero positivo...") 
                continue 
            return num 
        except ValueError: 
            print("Error, Numero invalido digite nuevamente...") 
            input("Presione cualquier tecla para continuar...") 

def leerPagoHora(msj): 
     while True: 
        try: 
            num = int(input(msj)) 
            if num == "" or num <1: 
                print("Digite un numero entero positivo...") 
                continue 
            return num 
        except ValueError: 
            print("Error, Numero invalido digite nuevamente...") 
            input("Presione cualquier tecla para continuar...")

def salario (horas , pagoHora): 

    if horas > 40: 
        extras = horas - 40
        pagoExtra = extras * (pagoHora*1.5)  
        horasRestantes = horas -extras 
        pago = horasRestantes * pagoHora 

        return pagoExtra + pago

    if horas < 40 :  
        pago = horas * pagoHora
        return pago

def leerPalabras(msj): 
    while True: 
        try: 
            parrafo = input(msj)  
            if parrafo == "": 
                print("Error. Digite nuevamente") 
                continue  
            numPalabras = parrafo.split() 
            longitud = len(numPalabras)
            return longitud 
        except Exception: 
            print("Error. Parrafo invalido") 
            input("Presione cualquier tecla para continuar...")

    



def menu (): 
    while True: 
        try: 
            print("*****MENU****") 
            print("1. Factorial de un numero") 
            print("2. Salario empleado") 
            print("3. Calcular palabras de un parrafo")  
            print("4. Salir")
            op = int(input("Digite de (1-4): ")) 
            if op == "" or op <1 or op >4: 
                print("Numero invalido digite un numero del 1 al 4")  
                input("Presione cualquier tecla para continuar...")
                continue 
            return op
        except ValueError: 
            print("Error. Numero invalido")
            input("Presione cualquier tecla para continuar... ") 

while True: 
    opcion = menu() 

    if opcion == 1: 
        print("Factorial de un numero") 
        fact = leerFactorial("Digite un numero entero positivo: ") 
        print(f"El factorial es: {factorial(fact)} ")

    elif opcion == 2: 
        print("Salario empleado")   
        horas = leerHoras("Digite el numero de horas trabajadas: ")
        pagoHora = leerPagoHora("Digite el pago por hora: ") 
        print(f"El pago por {horas} horas de trabajo es: $ {salario(horas , pagoHora):,.0f}")


    elif opcion == 3: 
        print("Calcular palabras de un parrafo")  
        palabras = leerPalabras("Digite el texto para realizar el conteo de palabras: ") 
        print(f"El numero total de palabras es: {palabras}")
    
    else: 
        print("Gracias por usar nuestra app") 
        input("Digite cualquier letra para salir...")
        break 
    input("Presione cualquier tecla para volver al menu ...") 
    print("\n", "=" *30)

