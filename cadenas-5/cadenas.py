#CADENAS 
#len se usa para saber la longitud del valor de una variable 

#Se coloca el nombre de la variable y luego entre [] se coloca la posicion de del caracter a acceder. 

s = "Yo soy tu padre"

print(s[7]) 
print(s[-8]) 

#Recorrido por indice porque estoy accediendo a cada posicion de la cadena se usa para saber la posicion 
 
for i in range(len(s)): 
    print(s[i] , end=", ") 


#Recorrido por elemento no por indices  

print("")
for e in s: 
    print(e ,end=", ") 

#SLICE  
#El primer parametro es desde donde empieza 
print("")
print(s[2:])  

#El primera parametros es desde , el segundo pararametro hasta, se cuenta uno menos 
print(s[4:7]) 

#Invertir una cadena
print( s[:: -1])

 
#Operador in 
print("tu" in s) 
print("yt" not in s)

#count 
print(s.count("o")) 

#find 
print(s.find("pa")) 
print(s.find("ma"))

# isdigit() da true si toda la cadena son digitos 
snum = "100" 
print(snum.isdigit()) 
snum = "100a"
print(snum.isdigit())

#split() ve el patron y parte la cadena 
nombre = "Juan David Caicedo Salazar" 
email = "daniel@gmail.com"
miles = "1.234.567"


print(nombre.split())
print(nombre.split("David")) 
print(email.split("@")) 
print(miles.split(".")) 

