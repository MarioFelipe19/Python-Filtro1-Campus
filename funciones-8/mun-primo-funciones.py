
def leerNumero(msj): 
    while True: 
        try:  
            num = int(input(msj))
            if num < 1 or num == "" : 
                print("Digite numeros positivos o algo") 
                continue 
            return num  
        except ValueError: 
            print("Error. Numeror invalido")
            
def numeroPrimo(num):   
    esPrimo = True
    
    for i in range (2 , num): 
        if num % i == 0: 
            esPrimo = False
             
        return esPrimo

def imprimirResultado(numero):
    if numero == False: 
        msj = "El numero no es primo" 
        return msj 

    else: 
        msj = "El numero es primo" 
        return msj


entrada = leerNumero("Digite un numero: ")  

numero = numeroPrimo(entrada)  
resultado = imprimirResultado(numero)

print(resultado)






