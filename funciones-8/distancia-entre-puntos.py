import math

("Punto 1")
 




def distancia(x2 , x1 , y2 ,y1): 

    d = math.sqrt((x1 - x2 )**2 + (y1 -y2)**2 )  
    return d     

def menu (): 

    print("Menu") 
    x1 = float(input("Digite la posicion de T en X1: "))
    y1 = float(input("Digite la posicion de T en y1: ")) 

    y2 = float(input("Digite la posicion de S en X2: "))
    x2 = float(input("Digite la posicion de S en y2: ")) 

    print(f"La distancia entre esos puntos es: {distancia(x2 , x1 , y2 ,y1):.1f}")  

menu() 




("Punto 2") 

def distancia(x2 , x1 , y2 ,y1): 

    d = math.sqrt((x2 - x1 )**2 + (y2 -y1)**2 )  
    return d      

def menu ():

    print("Menu") 
    x1 = float(input("Digite la posicion de T en X1: "))
    y1 = float(input("Digite la posicion de T en y1: ")) 

    y2 = float(input("Digite la posicion de S en X2: "))
    x2 = float(input("Digite la posicion de S en y2: ")) 

    rx = float(input("Digite la posicion de R en x: "))
    ry = float(input("Digite la posicion de R en y: "))    

    ts = distancia(x2 , x1 , y2 , y1 )  
    sr = distancia(x2 , rx , y2 , ry)   
    rt = distancia(x1 , rx , y1 , ry) 

    suma = ts + sr + rt 

    print(f"EL perimetro es: {suma:.1f}") 

menu()

("Punto 3 ") 

valor = 0



def leerValor ():  
    while True: 
        try: 
            print("Menu") 
            valorArt = int(input("Digite el valor del producto"))  
            if valorArt < 0 or valorArt =="": 
                print("Valor del producto invalido") 
                continue 
            return valorArt 
        except ValueError: 
            print("Error. Numero")




def calcularDescuento(val):
    descuento = 0
    if val > 150000:  
        descuento = val * 0.05  
    else: 
        descuento = 0  
    return descuento


valorArt = leerValor()  
descuento = calcularDescuento(valorArt)
print("El descuento es de : $", descuento)




("Punto 4") 


def calcularNota(nota ):  

    if nota / 5 >= 3.5:  
        msj = "Felicidades aprobaste"
        return msj 
    else: 
        msj = "Has reprobado" 
        return msj
    


def entradaNotas(): 
    nota = 0 
    totalNotas = 0 

    print("Notas") 
    while True: 
        try: 
           
            for i in range (1 , 6):   
                nota = float(input(f"Digite la nota {i}: "))  
                if nota < 0 or nota > 5 or nota == "": 
                    print("Error. Digite un numero entre 1 a 5") 
                    break
                totalNotas += nota 
            return totalNotas 
        except ValueError: 
            print("Error. Numero invalido ")  

totalNotas = entradaNotas() 
mensaje = calcularNota(totalNotas)  
print(mensaje)



