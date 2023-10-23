
from random import*

#Recorrer una matriz

l = [[1,2],[3,4],[5,6]] 

for f in range(len(l)): 
    for c in range(2): 
        print(l[f][c] , end=" ")  
    print()

#Crear una matriz 

a = []  
m = 3 
n = 2 

for f in range(m): 
    a.append([])

    for c in range(n):
        a[f].append(None)


for f in range(m): 
    for c in range(n): 
        print(a[f][c] , end=" ")  
    print() 


#Otra forma de crear una matriz con un numero aleatorio

fila = 3 
columna = 3 

matriz = [[randint(1,10)  for i in range(fila)] for j in range(columna)] 


for f in range(fila): 
    for c in range (columna): 
        print(matriz[f][c] , end=' ') 
    print() 



#Recorrer una matriz de forma iterativo o por elemento 

fila = 3 
columna = 3 

matriz = [[randint(1,10)  for i in range(fila)] for j in range(columna)]  

for f in matriz: 
    print(f) 


#Obtener una fila de una matriz 


f = int(input("Digite la fila a obtener")) 
b = [] 
for a in range(len(matriz)): 
    b.append(matriz[f][a]) 

print(b) 


# Obtener una columna 


c = int(input("Digite la columa a obtener")) 
m = [] 
for i in range(len(matriz)): 
    m.append(matriz [i][c]) 

print(m)