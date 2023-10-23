from random import* 

def leerNombre():  
    while True: 
        try: 
            n = input("Nombre? ")  
            n = n.strip()
            if n == "" or not n.isalnum():  
                print("Nombre invalido ..") 
                input("Presione entrer para continuar") 
                continue 
            return n 
        except Exception: 
            print("Error al digitar el nombre")
            input("Presione entrer para continuar") 

def buscarJugador(nombre , dicJugadores): 
    return nombre in dicJugadores

def leerInt (): 
            while True:
                try:
                    n = int(input("Numero ?"))
                    if n <= 0 or n == "":
                        print("Numero invalido")
                        continue
                    return n
                except ValueError:
                    print("Error al ingresarel numero") 

def verificarNumero(num , numeroMaquina): 
   
    if numeroMaquina < num:  
        return "El numero es menor al tuyo"  

    elif numeroMaquina > num:  
        return "El numero es mayor al tuyo" 

    else:  
        return True  

def ordenarDiccionario(lst):
    N = len(lst)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if lst[i][1]["intentos"] > lst[j][1]["intentos"]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
    return lst

def juego(dicJugadores , intentosJugador , numeroMaquina, nombre): 

    for i in range (1 , 10 + 1):
        input("Presiona enter para continuar")
        print("*" * 30)  
        print("Juego adivina el numero")   
        print("Intento " , i)  
        num = leerInt() 
        
        numVerificado = verificarNumero(num , numeroMaquina )  
        intentosJugador += 1
        
        dicJugadores[nombre]['intentos'] = intentosJugador 

        print(numVerificado) 

        if numVerificado == True: 

            print("Ganaste") 
            lstJugadores = list(dicJugadores.items()) 
            lstOrdenada = ordenarDiccionario(lstJugadores) 

            

            print(lstOrdenada) 
            diccionario = dict(lstOrdenada)
            del diccionario[nombre] ['JUGADOR']

            break

numeroMaquina = randint(1,10) 
eleccion = "s"

dicJugadores = {}

intentosJugador = 0 

while eleccion == "s": 

    dicDatos = {}
    nombre = leerNombre() 
    jugadorBuscado = buscarJugador(nombre , dicJugadores)   

    if jugadorBuscado == True: 
            print("El nombre de jugador ya existe")
            continue 
    
    dicJugadores[nombre] = dicDatos 

    while eleccion.lower() == "s":   

        numeroMaquina = randint(1,10) 

        dicDatos['JUGADOR'] = ""
        dicDatos['intentos'] = intentosJugador 
        

       
        juego(dicJugadores , intentosJugador , numeroMaquina , nombre) 

        lstJugadores = list(dicJugadores.items()) 
        lstOrdenada = ordenarDiccionario(lstJugadores) 
        

        eleccion = input("Desea continuar con su mismo perfil?  (s/n)") 

    eleccion = input("Desea continuar con otro nombre? (s/n)")
print("Muchas gracias por usar el software")

