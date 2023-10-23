#Calcular el factorial de un numero 
#Factorial de 5 = 1*2*3*4*5 

numero = int(input("Digite un numero")) 
factorial = 1

for i in range (1 , numero+1): 
    factorial *= i 

#EL f-string permite colocar dentro de una cadena de caracteres varable etc, le da formato
print(f"El factorial de {numero} es {factorial:,}")

