
conjunto = set()#Crea un conjunto vacio 
diccionario = {} 
diccionario2 = dict()

empleado = {"Nombre ":"Sergio Medina" , "cargo" : "programador" , "Salario" : 4000000} 

print(empleado["cargo"]) #Imprime el cargo
print(empleado.get("cargo")) #Imprime el cargo 

""" 
print(empleado["apellido"]) #Manda error 
print(empleado.get("apellido","llave no existe")) #Devuelve none porque no esta y permite devolver algo  """

#Si se desea delvolver un booleano o un numero se coloca como segundo parametro dentro de los () 

#Agregar  
empleado["sexo"] = "M" 
print(empleado)


#Modificar un valor 
empleado["Salario"] = 4500000 

#Borrar una llave y su valor 
del empleado["sexo"] 
print(empleado)

""" #Borrar todo el diccionario 
empleado = {} 
empleado.clear() 
del empleado #El del borra la variable empleado 
 """

oficina = empleado.copy()
print(oficina) 
oficina["salario"] = 500000 
print(oficina) 
print(empleado)

#Fromkeys  en el codigo del profe , 1er parametro da la llave y el 2do el valor a colocar en cada llave


#items crear par de tuplas , se usa para recorrer un diccionario , devulve un listado tipo tupla. 
print(empleado.items())  


#keys devulve un listado con todas la llaves 
print(empleado.keys()) 

#values devulve un listado con todos los valores del diccionario 
print(empleado.values()) 

""" #pop borra llave y valor de la llave colocada como parametro
print(empleado.pop("salario")) 
print(empleado)  """

#popitem item remueve la ultima llave insertada  
print(empleado.popitem()) 
print(empleado)

#setdefault si existe devulve el valor que ya existe, sino crea la llave con el valor
print(empleado.setdefault("Nombre" , "Carlos")) 
print(empleado.setdefault("Ciudad" , "Bucaramanga")) 
print(empleado)
