#1 Se usa coloca dentro de los [] una posicion y nos regresara cual es el elemento que esta en esa posicion 
s = "yo soy tu padre" 

""" 1 """ 
print(s[-8]) 


"Recorrido por indice (posicion-numero)"

for i in range (len(s) ) : 
    print(s[i] , end=",") 


print("")
"Recorrido por elemento (caracter)" 
for i in s : 
    print(i , end=",") 

"""Slice 
Se usa para recorrer la cadena de caracteres con tres parametros [inicio , fin , aumento-disminucion]
""" 
print()
print(s[0:4]) 
print(s[4:])
print(s[::1]) #viaja por toda la cadena 
print(s[::-1]) #viaja por toda la cadena al revez  

#Operador in 
print("tu" in s) #Si "tu" esta en la variable retorna true
print("yt" not in s) #Si "yt" no esta en la variable retorna true

#count 
#Cuenta cuantas veces aparece una subcadena en una cadena, una palabra en un frase 
print(s.count("o")) 

#find 
print(s.find("padre")) #Si se esncuentra o es verdadero devolvera su poscion en indice-numero desde donde empieza el parametro
print(s.find("ma")) #Si es falso o no se encuentra retorna un -1 

# isdigit() da true si toda la cadena son digitos 
snum = "100" 
print(snum.isdigit()) 
snum = "100a"
print(snum.isdigit())



"""
#EJERCICIOS PROPIOS

"Palabra polindraba" 

s = str(input("Digite una palabra para saber si es polindraba: "))  

reves = s[::-1]

if s.isalpha():
    if s == reves : 
        print(f"La palabra {s} es polindraba") 
    else: 
        print(f"La palabra '{s}' no es polindraba")
else: 
    print("La palabra no cumple con los parametros") 


"Fecha de nacimiento" 

fecha = input("Digite la fecha de nacimiento con el siguiente formato dd/mm/aaaa: ") 
partes = fecha.split("/") 

if partes[0].isdigit() and len(partes[0]) == 2 or len(partes[0]) == 1 and \
    partes[1].isdigit() and len(partes[1]) == 2 or len(partes[1]) == 1  and \
     partes[2].isdigit() and len(partes[2]) == 4 : 

    print(f"El dia es: {partes[0]} , el mes es: {partes[1]} y el año es: {partes[2]}") 
else: 
    print("El formato es incorrecto")
    
"""    
#Prefijo-numero-extension telefono 

num= str( input("Digite el numero con el siguiente formato +34-numero-56:  ")) 

partesTel= num.split("-") 

if num.startswith("+") and partesTel[1].isdigit() and \
    partesTel[0] == "+34" and partesTel[2] == "56" and num.count("-") == 2:  
    
    print(f"El numero es: {partesTel[1]} " )  
    numero = int(partesTel[1]) 
    print(type (numero))
else: 
    print("Formato incorrecto")