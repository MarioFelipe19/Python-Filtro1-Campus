#Defirnir la funciòn
def longString(str): 
    try:
        long = 0 
        while str[long] != None: 
            long += 1
    except: 
        pass #no haga nada - pasa de largo  
    return long

def preparaCafe(insumo1, insumo2): 
    salida = "" 
    if insumo1.lower() == "cafe" and insumo2.lower() == "agua": 
        salida = "tinto" 
    else: 
        salida = "Daño la cafetera"  
    return salida

#Usar la funciòn 
taza = preparaCafe("cafe" , "agua") 

print(taza) 

print(longString(taza))
