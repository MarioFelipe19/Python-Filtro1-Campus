def quitarTexto(msj): 
    while True: 
        try:
            cadena = input(msj) 
            if cadena == "":  
                print("Texto invalido digite denuevo")
                continue
            for i in cadena: 
                if i.isdigit() == False: 
                    cadena = cadena.replace(i , "") 
            return cadena 
        except Exception as e: 
            print("Error. Cadena invalida " , e)
        
def leerNum(msj): 
     while True: 
        try: 
            numero = int(input(msj)) 
            if numero == "" or numero < 1: 
                print("Digite un numero positivo entero") 
                input("Presione cualquier tecla para continuar...") 
                continue  
            return numero 
        except ValueError:  
            print("Error. Numero invalido") 
            input("Presione cualquier tecla para continuar...") 

 
def factorial(numero): 
    factorial = 1

    for i in range (1 , numero+1): 
        factorial *= i 

    return factorial
    

def leerIva(msj): 
    while True: 
        try:
            num = float(input(msj)) 
            if num == "" or num <= 0: 
                print("Numero invalido")
                input("Presione cualquier tecla para continuar...") 
                continue
            return num 
        except ValueError : 
            print("Error. Numero invalido") 
            input("Presione cualquier tecla para continuar...") 

def leerValor(msj): 
    while True: 
        try: 
            valor = int(input(msj)) 
            if valor == "" or valor < 1: 
                print("Numero invalido.") 
                continue 
            return valor 
        except ValueError: 
            print("Error. Numero invalido") 
            input("Presione cualquier tecla para salir ... ")  

def factura(iva , valor): 

    ivaFinal = valor * (iva/100)  

    valorFinal = ivaFinal + valor

    return valorFinal    

def combinar(num1 , num2):  

    #n! / ((n - m)! * m!) 
    resta = num1 -num2
    numero = factorial(num1)/ (factorial(resta) * factorial(num2))
    return numero

def menu(): 

    while True: 
        try: 
            print("\n*****Menu*****")
            print("1. Calcular combinatoria") 
            print("2. Convertir texto a numero")
            print("3. Calcular iva de una factura") 
            print("4. Salir")  
            op = int(input(">>>>>> Opcion (1-4): ")) 
            if op <1 or op > 4: 
                print("Opcion no valida. Escoja de 1 a 4. ")  
                input("Presione cualquier tecla para continuar: ")
                continue 
            return op #Devulve el valor op 
        except ValueError:  
            print("Errono. Opcion invalida...") 
            input("Presione cualquier tecla para continuar: ")

while True: 

    opcion = menu() 

    if opcion == 1: 
        print("\n\n1.Calcular combinatoria") 
        num1 = leerNum("Ingrese la cantidad de objetos base: ") 
        num2 = leerNum("Ingresa la cantidad de objetos a escoger sobre esa base: ")   
        print(f"La combinatoria de es {combinar(num1 , num2)}") 

    elif opcion == 2: 
        print("\n\nConvertir texto a numero ") 
        cadena = quitarTexto("Digite la cadena de texto: ") 
        print(f"La cadena en numeros es: {cadena}")  
        input("Presione cualquier tecla para continuar: ")

    
    elif opcion ==3:  
        print("\n\n3. Calcular iva de una factura") 
        iva = leerIva("Digite el iva de la factura: ") 
        valor = leerValor("Digite le valor de la factura: ")  
        print(f"El valor de la factura es {factura(iva , valor)}")
    
    elif opcion == 4:  
        print("\n\nGracias por usar el codigo") 
        print("Adios") 
        input("Presione cualquier tecla para salir ... ") 
        break 









