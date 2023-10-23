#Ciclo for - para 
# for variable en "rango de"

 
for i in range(10): 
    #end="como quiero que termine"
    print(i , end="-")  
    
print("")
      
 
for i in range(5): 
    print("*" , end="")

for i in range(3): 
    print("*    *" )

for i in range(6): 
    print("*" , end="")  
    
input() 

 

cantidadLineas= int(input("\nDigite la cantidad de lineas: ")) 


for i in range (cantidadLineas):  
    for j in range (i + 1):
        print("*" , end="")  

    print()
      



