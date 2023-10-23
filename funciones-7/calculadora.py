def suma (num1 , num2): 
    resultado = num1 + num2 
    return resultado 

def resta (num1 , num2): 
    return num1 - num2

def mult (num1 , num2): 
    return num1 * num2 

def dividir (num1 , num2):  
    try: 
        resultado = num1 / num2  
    except ZeroDivisionError: 
        resultado = None 
    return resultado

def menu(): 

    while True: 
        try: 
            print("*****MENU CALCULADORA****") 
            print("1. Sumar") 
            print("2. Restar") 
            print("3. Multiplicar") 
            print("4. Dividir") 
            print("5. Salir") 
            op = int(input(">>>>>> Opcion (1-5): ")) 
            if op <1 or op > 5: 
                print("Opcion no valida. Escoja de 1 a 5. ")  
                input("Presione cualquier tecla para continuar: ")
                continue 
            return op #Devulve el valor op 
        except ValueError:  
            print("Opcion no valida. Escoja de (1-5 )") 
            input("Presione cualquier tecla para continuar: ") 
    
def leerNum(mensaje): 
    while True: 
        try:
            num = float(input(mensaje))
            return num 
        except ValueError : 
            print("Error. Numero invalido") 
            input("Presione cualquier tecla para continuar...")
    
#Programa principal 
while True: 

    opcion = menu() 
    

    if opcion == 1: 
        print("\n\n1. Sumar")  
        num1 = leerNum("Ingrese el primer numero: ") 
        num2 = leerNum("Ingrese el segundo numero: ") 
        print(f"El resultado de la suma es: {suma(num1 , num2):.2f}")
       
    elif opcion == 2:
        print("\n\n1. Restar")  
        num1 = leerNum("Ingrese el primer numero: ") 
        num2 = leerNum("Ingrese el segundo numero: ") 
        print(f"El resultado de la resta es: {resta(num1 , num2):.2f}")

    elif opcion == 3: 
        print("\n\n1. Multiplicar")  
        num1 = leerNum("Ingrese el primer numero: ") 
        num2 = leerNum("Ingrese el segundo numero: ") 
        print(f"El resultado de la multiplcacion es: {mult(num1 , num2):.2f}")

    elif opcion == 4: 
        print("\n\n1. Dividir")  
        num1 = leerNum("Ingrese el primer numero: ") 
        num2 = leerNum("Ingrese el segundo numero: ") 
        resultado = dividir(num1, num2 ) 
        if resultado != None: 

            print(f"El resultado de la division es: {resultado:.2f}") 
        else: 
            print("La division entre cero es indeterminado")

    elif opcion == 5: 

        print("\n\nGracias por usar la calculadora") 
        print("Adios") 
        input("Presione cualquier tecla para salir ... ") 
        break 
    input("Presione cualquier tecla para volver al menu ...")
    
