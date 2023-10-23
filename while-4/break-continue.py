#Break
#Calcular si es un numero es primo  
# num primo : divisible por si mismo y por 1 

num = int(input("Ingrese un numero: ")) 

if num < 2: 
    print("no es primo") 

elif num == 2: 
    print("Es primo") 
else: 

    esPrimo = True #Variable bandera o de tipo switch

    for i in range(2 , num): 
        if num % i == 0: 
            esPrimo = False
            break 

    if esPrimo == True: 
        print(f"El numero {num} es primo ") 
    else: 
        print("No es primo es divisible por: " , i)
         
#CONTINUE 
#Saltar interaccion de un ciclo 

#Imprima los numeros al 100 excepto los multiplos de 7
for i in range(1,100): 
    if i % 7 == 0 : 
        continue

    print(i , end=",")