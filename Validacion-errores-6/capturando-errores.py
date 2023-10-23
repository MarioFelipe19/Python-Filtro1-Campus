while True:
    while True:
        try:
            num1 = int(input("Digite un numero: ")) 
            break

        except ValueError: 
            print("Error. Numero enteno no valido")

    while True:

        try:
            num2 = int(input("Digite otro numero: ")) 
            break

        except ValueError: 
            print("Error. Numero enteno no valido")  

    try: 
        
        suma = num1 + num2  
        print("La suma es: " , suma)
        break  

    #El error se pasa a llamar "e"

    except Exception as e: 
        print("Error al intertar sumar. \n" , e)


