import json 
import time 

def leerInt(jugador): 
    while True: 
        try: 
            op = int(input(f"{jugador}: "))
            if op == "" or op < 1 or op > 9: 
                print("Error opcion invalida") 
                input("Presione enter para continuar") 
                continue
            return op 
        except ValueError: 
            print("Error al digitar la opcion") 
            input("Presione enter para continuar")  


def guardarDatos (lstJugadores , ruta):  
    try: 
        fd = open(ruta , "w") 
    except Exception as e: 
        print("Error al abrir el archivo para guardar al jugador\n" , e) 
        return None
    
    try: 
        json.dump(lstJugadores, fd) #Carga el archivo
    except Exception as e: 
        print("Error al guardar la informacion del jugador\n" , e)
        return None

    fd.close() 
    return True

def cargarInfo(lstJugadores , ruta): 
    try: 
        fd = open(ruta, "r") #Fd es la la apertura del archivo
    except Exception as e:  

        try: 
            fd = open(ruta , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": #Si tiene el archivo algo de contenido cargara los datos, sino creara una lista vacia.
            fd.seek(0)
            lstJugadores = json.load(fd) 
        else: 
            lstJugadores = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None 
    
    #print(lstJugadores)
    fd.close() #Si se carga todo cierre el archivo
    return lstJugadores #Deculve la lista cargada 

def existeNombre(jugador , lstJugadores): 
    for datos in lstJugadores:  
        k = list(datos.keys())[0] #Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente
        if k == jugador: 
            return True 
    return False


instrucciones = """ 

Este sera el tablero del juego 

  1  |  2  |  3
-----|-----|-----
  4  |  5  |  6
-----|-----|-----
  7  |  8  |  9 


Instrucciones de juego 
1ro : Debes digitar el numero de la casilla que deseas rellenar (1/9) 
2do : Si llega a ver un empate el resultado de solo se mostrara cuando se llenen todos los espacios.
3ro : El jugador uno empieza la partida

"""
listaPosiciones = [] 
signDiccionario = []  

for i in range(1 , 10): 
    signDiccionario.append(i)  

""" def ordenarTabla(lst):  
    N = len(lst)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if lst[i][1]["tiempo"] < lst[j][1]["tiempo"]:
                t = lst[1]
                lst[i] = lst[j]
                lst[j] = t 
    
    return lst """
    

def tablaPosiciones(lst):    

    listaOrd = ordenarLista(lst)
    print("Posicion \t NOMBRE \tIntentos \tTiempo")

    for i in range(len(listaOrd)):
        datos = listaOrd[i]
        k = list(datos.keys())[0]
        for d in listaOrd[i]:
            print(f"{i+1}\t\t{k} \t\t{listaOrd[i][d]['intentos']}\t\t{listaOrd[i][d]['tiempo']}")  
            input()   


def ordenarLista(lstLibros):
    n = len(lstLibros)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstLibros[j].items())[0][1]['intentos']
            k1 = list(lstLibros[j+1].items())[0][1]['intentos']
            # print(list(lstLibros[j].items())[0][1])
            # print("K, K+1, : ", k, k1, ) 

            if k == 0 : 
                del lstLibros[j] 

                guardarDatos(lstJugadores , ruta) 
                    
            if k1 == 0:  
                del lstLibros[j+1]

                guardarDatos(lstJugadores , ruta) 
                    

            if k > k1:
                lstLibros[j], lstLibros[j+1] = lstLibros[j+1], lstLibros[j]
                intercambio = True 
            
            
                
        if intercambio == False: 
            kt = list(lstLibros[j].items())[0][1]['tiempo']
            k1t = list(lstLibros[j+1].items())[0][1]['tiempo'] 
            #print("K, K+1, : ", kt, k1t, ) 
            #input()

            if kt > k1t:
                lstLibros[j], lstLibros[j+1] = lstLibros[j+1], lstLibros[j]
                intercambio = True

                    # t= lstLibros[i]
                    # lstLibros[i] = lstLibros[j]
                    # lstLibros[j] = t
            break
    return lstLibros

def eliminarJugador(lstJugadores , ruta , jugador):  
    for i in range(len(lstJugadores)): #Busqueda por posicion
        datos = lstJugadores[i]
        #print(jugador)
        #print(datos)
        k = list(datos.keys())[0]
        #print(k)
        #input()

        if k == str(jugador): 
            del lstJugadores[i]  
            #print(lstJugadores)
            #input()
    
            # if guardarDatos(lstJugadores , ruta) == True: 
            #     print("El jugador ha sido borrado con exito") 
            # else: 
            #     print("Ocurrio un error al borrar al jugador") 
            # break

def imprimirTablero(): 
    
    tablero = f"""
    
  {signDiccionario[0]}  |  {signDiccionario[1]}  |  {signDiccionario[2]}
-----|-----|-----
  {signDiccionario[3]}  |  {signDiccionario[4]}  |  {signDiccionario[5]}
-----|-----|-----
  {signDiccionario[6]}  |  {signDiccionario[7]}  |  {signDiccionario[8]} 

    """ 

    print(tablero) 

indexList = []
def tomarEntrada(jugador): 
    while True: 
        x = leerInt(jugador)
        x -= 1  
        if 0 <= x < 10: 
            if x in indexList: 
                print("Esta casilla no esta disponible") 
                continue
            indexList.append(x) 
            return x
        print("Ingresa un numero del 1 al 9")

def calcularResultado(jugadorUno, jugadorDos , lstJugadores , ruta , signoJugUno , signoJugDos): 

    if signDiccionario[0] == signDiccionario[1] == signDiccionario[2] == signoJugUno or signDiccionario[1] == signDiccionario[4] == signDiccionario[7] == signoJugUno or signDiccionario[0] == signDiccionario[4] == signDiccionario[8]== signoJugUno  or signDiccionario[2] == signDiccionario[5] == signDiccionario[8]== signoJugUno or signDiccionario[3] == signDiccionario[4] == signDiccionario[5]== signoJugUno or signDiccionario[2] == signDiccionario[4] == signDiccionario[6]== signoJugUno or signDiccionario[6] == signDiccionario[7] == signDiccionario[8]== signoJugUno or signDiccionario[0] == signDiccionario[3] == signDiccionario[6]== signoJugUno:  
        print(f"Felicidades jugador {jugadorUno} ha ganado") 
        eliminarJugador(lstJugadores , ruta , jugadorDos)
        quit()

    elif signDiccionario[0] == signDiccionario[1] == signDiccionario[2] == signoJugDos or signDiccionario[1] == signDiccionario[4] == signDiccionario[7] == signoJugDos or signDiccionario[0] == signDiccionario[4] == signDiccionario[8]== signoJugDos  or signDiccionario[2] == signDiccionario[5] == signDiccionario[8]== signoJugDos or signDiccionario[3] == signDiccionario[4] == signDiccionario[5]== signoJugDos or signDiccionario[2] == signDiccionario[4] == signDiccionario[6]== signoJugDos or signDiccionario[6] == signDiccionario[7] == signDiccionario[8]== signoJugDos or signDiccionario[0] == signDiccionario[3] == signDiccionario[6]== signoJugDos:  
        print(f"Felicidades jugador {jugadorDos} ha ganado") 
        eliminarJugador(lstJugadores , ruta , jugadorUno) 
        quit()


    
def programaPrincipal (lstJugadores , ruta):  
    
    print("=" * 10 , "TIC TAC TOE" , "=" * 10 )  

    dicDatosUno = {} 
    jugadorUno = input("Ingrese su nombre jugador uno: ")   

    if existeNombre(jugadorUno , lstJugadores) == True or jugadorUno == "": 
        print(f"El nombre {jugadorUno} ya existe o es invalido") 
        input()
        return

    dicDatosUno[jugadorUno] = {"intentos": 0 , "tiempo":0}
    lstJugadores.append(dicDatosUno) 


    #print(lstJugadores) 
    
    dicDatosDos = {}
    jugadorDos =input("Ingrese su nombre jugador dos: ")   

    if existeNombre(jugadorDos , lstJugadores) == True or jugadorUno == "" : 
        print(f"El nombre {jugadorDos} ya existe o es invalido")  
        input()
        return

    dicDatosDos[jugadorDos] = {"intentos":0 , "tiempo":0} 
    lstJugadores.append(dicDatosDos) 

    #print(lstJugadores)  

    if guardarDatos(lstJugadores , ruta) == True: 
        
        input("Los jugadores han sido agregado con exito") 
    else: 
      input("Ocurrio algun error al guardar el empleado")

    #guardarDatos(lstJugadores , ruta)
    
    print(f"\nEl jugador {jugadorUno} se enfretara a el jugador {jugadorDos}\n") 

    input("Presiona enter para ver las instrucciones de juego")
    print(instrucciones) 

    input("Presione enter para jugar") 

    imprimirTablero()
    
    contJugUno = 0
    contJugDos = 0 
    totalJugUno = 0 
    totalJugDos = 0 
    tiempoTotalUno = 0 
    tiempoTotalDos = 0

    

    ficha = input("Jugador uno con que ficha desea jugar ? (x/o)")

    signoJugUno = "x"
    signoJugDos = "o" 

    if  ficha == "" or not ficha.isalpha(): 
        print("Digite x/o")  
        input()
        eliminarJugador(lstJugadores , ruta , jugadorUno) 
        eliminarJugador(lstJugadores , ruta , jugadorDos) 
        return

    if ficha.lower() == "o": 
        signoJugUno = "o"
        signoJugDos = "x"

    for i in range(9): 

        if i % 2 ==  0: 
            comienzoJugUno = time.time()
            index = tomarEntrada(jugadorUno) 
            contJugUno += 1
            signDiccionario[index] = signoJugUno
            finJugUno = time.time()  
            totalJugUno += finJugUno-comienzoJugUno 
            tiempoTotalUno = f"{totalJugUno:.1f}"
               
        else: 
            comienzoJugDos = time.time()
            index = tomarEntrada(jugadorDos) 
            contJugDos += 1
            signDiccionario[index] = signoJugDos 
            finJugUno = time.time()  
            totalJugDos += finJugUno-comienzoJugDos 
            tiempoTotalDos = f"{totalJugDos:.1f}"
            
            

        imprimirTablero() 
        dicDatosUno[jugadorUno]["intentos"] = contJugUno 
        dicDatosDos[jugadorDos]["intentos"] = contJugDos  

        dicDatosUno[jugadorUno]["tiempo"] = float(tiempoTotalUno) 
        dicDatosDos[jugadorDos]["tiempo"] = float(tiempoTotalDos) 
        

        guardarDatos(lstJugadores , ruta)
            
        calcularResultado(jugadorUno, jugadorDos , lstJugadores , ruta , signoJugUno , signoJugDos ) 
          
   
    eliminarJugador(lstJugadores , ruta , jugadorUno) 
    eliminarJugador(lstJugadores , ruta , jugadorDos)

    print("Esto es un empate")
          

#Programa menu y listas

lstJugadores = [] 
ruta = "Tic Tac Toe/jugadores.json" 
lstJugadores = cargarInfo(lstJugadores, ruta)   

def menu ():  
    while True:
        try:
            print("*** TIC TAC TOE DE ACME ***".center(40))
            print("MENU".center(40))
            print("1.Jugar dos jugadores ")
            print("2.Consultar tabla de posiciones")  
            print("3.Salir")
            
            
            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. ")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. ")
            input("Presione cualquier tecla para continuar...") 

    
while True:

    op = menu()

    if op == 1:
        programaPrincipal( lstJugadores , ruta )
    elif op == 2:
        tablaPosiciones(lstJugadores) 
    elif op == 3: 
        print("Gracias por usar el juego\nAdios")
        break

    
    
    








