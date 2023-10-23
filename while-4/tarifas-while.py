eleccion = "S" 
tarifaBasica = 0

while eleccion == "S" or eleccion == "s":  

    nombre = input("Digite el nombre del usuario: ") 
    estrato = int(input("Digite el estrato [1-5]: ")) 

    if estrato == 1:  
        tarifaBasica = 10000

    if estrato == 2:  
        tarifaBasica = 15000

    if estrato == 3:  
        tarifaBasica = 30000

    if estrato == 4:  
        tarifaBasica = 50000

    if estrato == 5:  
        tarifaBasica = 65000
    
    print("\n" , "=" * 30)

    print(f"Nombre del usuario : {nombre}\nTarifa basica $ {tarifaBasica:,.0f}") 

    print("\n" , "=" * 30)

    eleccion = input("Desea seguir facturando? [S-s] sino digite cualquier otra cosa: ") 

    print("\n" , "=" * 30)
    
print("Muchas gracias")