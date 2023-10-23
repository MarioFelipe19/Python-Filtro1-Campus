
def leerFecha(msj): 
    while True: 
        try : 
            fecha = input(msj) 
            partes = fecha.split("/") 

            if not partes[0].isdigit() or len(partes[0]) > 2 or len(partes[0]) < 1 or \
            not partes[1].isdigit() or len(partes[1]) > 2 or len(partes[1]) < 1  or \
            not partes[2].isdigit() or len(partes[2]) > 4 or len(partes[2]) < 1 :   
                print("Fecha invalida, digite nuevamente") 
                input("Presione cualquier tecla para continuar: ") 
                continue 
            return partes                     
        except Exception as e:  
            print("Error. Fecha invalida " , e) 
            input("Presione cualquier tecla para continuar: ") 


partes = leerFecha("Digite la fecha de nacimiento con el siguiente formato dd/mm/aaaa:") 

print(f"El dia es: {partes[0]} , el mes es: {partes[1]} y el año es: {partes[2]}") 



