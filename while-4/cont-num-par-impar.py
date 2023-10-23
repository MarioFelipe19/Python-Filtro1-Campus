#Contador de numeros pares e impares 

num = int(input("Ingrese un numero : "))
print("Si el numero es -1 el programa se cierra") 
input()
cPares = 0 
cImpares = 0

while num != -1 : 
    if num % 2 == 0: 
        print("EL numero es par")  
        cPares += 1

    else : 
        print("El numero es impar") 
        cImpares += 1 

    num = int(input("Ingrese un numero: "))

print("\n" , "="  *30) 
print("La cantidad de numeros pares: " , cPares) 
print("La cantidad de numeros impares es: " , cImpares) 
