
def calcProdMaxIngresosSem(matVentas , matPrecios):
    fil = len(matVentas) #Nos da la cant de filas 
    lstTotVtas = [0] * fil 
    
    for f in range(fil):  
        lstTotVtas[f] = sum(matVentas[f])* matPrecios[f] 

    #print(lstTotVtas)
    maxVtas = max(lstTotVtas)#Devuelve el valor mas alto
    proMaxVentas = lstTotVtas.index(maxVtas) + 1
    return proMaxVentas

def calcDiaMayorVentas(matVentas , matPrecios):  
    fil = len(matVentas) 
    colum = len(matVentas[0])
    lstDiaVentas = [0] * colum

    for f in range(fil): 
        for c in range (colum):
            lstDiaVentas[c] += matVentas[f][c] * matPrecios[f] 

    maxDiaVenta = max(lstDiaVentas)
    posMaxDiaVentas = lstDiaVentas.index(maxDiaVenta) 

    
    return posMaxDiaVentas




matPrecios = [1500 , 5000 , 6500 , 2500 , 22500] 
matVentas =[ [100, 88, 92, 94, 85, 110, 118], 
             [30, 42, 31, 31, 38, 40, 37],
             [23, 35, 39, 45, 55, 60, 61], 
             [45, 50, 56, 65, 47, 57, 68], 
             [18, 25, 33, 21, 22, 28, 32] ]

prodMaxIngSem = calcProdMaxIngresosSem(matVentas , matPrecios) 
diaMayorVenta = calcDiaMayorVentas(matVentas , matPrecios) 

dias = ["Lunes" , "Martes" , "Miercoles" , "Jueves" , "Viernes" , "Sabado" , "Domingo"]

print("El producto que mas genera ingresos en la semana es: " , prodMaxIngSem) 
print("El dia que mas vende es el:" , dias[diaMayorVenta])