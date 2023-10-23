#Numero perfecto
print("Punto 1 ")

suma = 0

numero = int(input("Digite el numero: "))

for i in range (1 , numero): 
    if numero%i == 0: 
        suma += i 
if numero == suma :  
    print("El numero es perfecto") 
else: 
    print("EL numero no es perfecto")


#Numero primo
print("Punto nada") 
cantNum = int(input("Cuantos numeros desea ingresar: "))   


for i in range( 1 , cantNum + 1 ): 

    numero = int(input("Digite un numero positivo: ")) 

    if numero%(i) == 0: 
            print("EL numero no es primo")  

input()

print("Punto 2")  

matricula = 10000 
incremento = 0.07  
suma = 0
años = 0

while matricula <= 20000: 
    suma = matricula*incremento 
    matricula += suma  
    años += 1
    print(f"Para el año: {años:} la matricula vale: $ {matricula:,.1f} " )
print("Tarda tantos:",años) 



print("Punto 3") 


import random 
num = 1000000 
numHits = 0  

for i in range (num) : 
    x = random.uniform(-1 , 1) 
    y = random.uniform(-1 , 1) 

    if(x**2+y**2 < 1) : 
        numHits += 1 
        
print(numHits) 
print((4*numHits)/1000000)






