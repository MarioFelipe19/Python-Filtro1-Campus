milista = [] #Lista vacia
milista = list() #Lista vacia 

nomCampers = ["Juan" , "Yulieth" , "Lorenzo" , "Manuel" , "David"]

print(nomCampers) 
print(nomCampers[1])  
nomCampers[1] = "Julieth" #Modificar la posicion 1
print(nomCampers[1]) 

#SLICES 
print(nomCampers[2:4]) #Del 2 al 3 no cuenta el 4 
print(nomCampers[::-1]) #Imprimir de forma invertida 

nomCampers_juan = ["Daniel" , "Maria" , "Juliana" , "Sandra" ,  "Carolina"] 
print(nomCampers_juan)
nomCampers += nomCampers #Concatenar las dos listas
print(nomCampers)
    
#Metodos   

#Append
nomCampers.append("Kevin") #Agregar al final 
print(nomCampers)  

#Extend
nomCampers.extend(nomCampers_juan)#Extender un arreglo
print(nomCampers) 
print(nomCampers[-1])

#Insert inserta un elemento en la lista 

nomCampers.insert(1 , "Carlos")#Posicion - Valor a colocar 
print(nomCampers) 

#Pop elimina 

nomCampers.pop()#Si no dice nada elimina el ultimo elemento 
print(nomCampers) 

nomCampers.pop(-3) 
print(nomCampers) 

#Remove 
nomCampers.remove("Sandra") #Elimina un elemento por su elemento
print(nomCampers) 

#Sort ordena alphabeticamente  

nomCampers.sort() 
print(nomCampers) 

nomCampers.insert(2,"Daniel") 
nomCampers.sort() 
print(nomCampers) 


""" list2 = [0,1,15,"155"] 
list2.sort() 
print(list2) """ 

nomCampers.sort(reverse=True)#Ordena de desendente a ascendente 
print(nomCampers)