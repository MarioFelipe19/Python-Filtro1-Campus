
def leerCiudad(msj): 
    while True: 
        try: 
            c = input(msj)  
            if c.lower() in matCiudades and c.lower() in matCiudades: 
                return c  
            else: 
                print("La ciudad no existe")
                continue  
        except Exception: 
            print("Error al ingresar la ciudad")

    
def posicionOrigen(ciudadOrigen, matCiudades):  

    for ciudadOrigen in matCiudades: 
        if ciudadOrigen == ciudadOrigen: 
            pos = matCiudades.index(ciudadOrigen) 
            return pos
    
def verificarConexiones(pos , matEnlaces): 
    bandera = False 
    for posicion in matEnlaces[pos]: 
        

        if ciudadDestino == posicion: 
             bandera = True 
            
    return bandera


matEnlaces = [["ubate" , "villavicencio"],
              ["bogota" , "mitu"],
              ["bogota" , "leticia"],
              ["villavicencio" , "mitu"] , 
              ["leticia" , "villavicencio"]]

matCiudades= ["bogota" , "ubate" , "villavicencio" , "leticia" , "mitu"] 



ciudadOrigen=leerCiudad("Ciudad origen? ")
ciudadDestino=leerCiudad("Ciudad destino? ") 


posicion = posicionOrigen(ciudadOrigen, matCiudades)




if verificarConexiones(posicion , matEnlaces) == True: 
    print(f"Ha conexion directa entre {ciudadOrigen} y {ciudadDestino}") 
else: 
    print(f"No hay conexion directa entre {ciudadOrigen} y {ciudadDestino}")





        





