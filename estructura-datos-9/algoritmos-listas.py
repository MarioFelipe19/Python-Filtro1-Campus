def findElementListPos(lst , elem):  
    #Funcion qur busca un elemento en la lista 
    #Si lo encunetra devuelve la posicion 
    #Si no lo encuentra de vuelve -1
    for p in range(len(lst)):  
        if elem == lst[p]: 
            return p   
        
    return -1 #Si no esta retorno -1
        
def existElemList(lst , elem):  
    #Funcion qur busca un elemento en la lista 
    #Si lo encunetra devuelve la true 
    #Si no lo encuentra de vuelve false  

    for e in lst: 
        if e == elem: 
            return True 
        
    return False





    

