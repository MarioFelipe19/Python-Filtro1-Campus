lst = [1,2,3,4,5,4,3,2,1] 

#Imprimir los elementos de la lista
for n in lst: 
    print(n , end="-") 


for n in range(len(lst)): 
    print(n) 


#Saber la posicion de num en la lista de numeros
num = 5
for n in lst:
    if num == n:  
        pos = lst.index(n)
        print(f"EL numero {num} esta en la posicion: {pos}")
