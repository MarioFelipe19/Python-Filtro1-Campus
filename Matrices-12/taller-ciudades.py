          
def verificarCiudad(ciudad, matCiudades ):  
    fil = len(matCiudades) 
    colum = len(matCiudades[0]) 

    for f in range(fil): 
        for c in range (colum):
            if ciudad == matCiudades[f][c]:  
                return "La ciudad existe"  
            
            
        
def verificarEnlaceCiudad (origen , destino): 
    pass 

    
def posicionOrigen(origen , matCiudades):  
        fil = len(matCiudades) 
        for i in range(fil): 
            if origen == i: 
                return i  


#Programa principal
                   
matCiudades = [["leticia"],
               ["bogota"],
               ["medellin"], 
               ["barranquilla"],
               ["villavicencio"]]  

print("Ciudades disponibles: " , matCiudades )

ciudOrig = input("Ciudad de origen? ") 
verCiudOrig = verificarCiudad(ciudOrig , matCiudades)  

if verCiudOrig == None: 
     verCiudOrig = "La ciudad no existe" 
     print(verCiudOrig) 
else: 
     print(verCiudOrig)


ciudDest = input("Ciudad destino ? ") 
verCiudDest = verificarCiudad(ciudDest , matCiudades)   

if verCiudDest == None: 
     verCiudDest = "La ciudad no existe" 
     print(verCiudDest) 
else: 
     print(verCiudDest)

posicionOrigen(verCiudOrig , matCiudades)

verificarEnlaceCiudad(verCiudOrig,verCiudDest)



matEnlaces = [["bogota", "villavicencio"],
            ["medellin" ,"villavicencio"],
            ["bogota" , "barranquilla"], 
            ["medellin","bogota"], 
            ["bogota","leticia"]]




    
