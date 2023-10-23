import math  

#Cada digito que tiene un numero

num1 = int(input("Digite un numero entero positivo: ")) 

if num1 < 0 : 
    num1 *= -1 

# Math.floor() Redondea todo numero a la parte inferior 3.99 a 3
cantDigitos = math.floor(math.log10(num1)) + 1 

print("La cantidad de digitos es: " , cantDigitos) 
