
#Ordenamiento burbuja

def ordenamiento_burbuja(lst): 
    n = len(lst) 

    pass


productos = {

    1: {
        'nombre' : "pantalon",
        'precio' : 125, 
        'cantidad' : 5
    },

    2: {
        'nombre' : "zapatos",
        'precio' : 100, 
        'cantidad' : 20
    },

    3: {
        'nombre' : "camisa",
        'precio' : 30, 
        'cantidad' : 12
    }
} 

print(productos) 

#PASAR DEC A LISTA 
#Uno el lis() para convertir el diccionario a lista
print() 
lstproductos = list(productos.items())
print(lstproductos) 

lstOrdenada = ordenamiento_burbuja(lstproductos)

#COnvertir a diccionario
print("")
productos = dict(lstOrdenada)
print(productos)