def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip("")
            if nom == "" or nom != "mbox.txt":
                print("Nombre inválido o no existe el archivo")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e) 

def calcularPromedio( sumatorio, ct ) : 
    return sumatorio / ct

def calcularSpam(lstDatos,sumatorio): 
    for num in lstDatos: 
        sumatorio += float(num)  
    return sumatorio

nombre = leerNombre("Digite el nombre del archivo: ") 
ruta = "Test-2/mbox.txt"


fd = open(ruta , "r")  

ct = 0
lstDatos = [] 
sumatorio = 0

try: 

    for linea in fd: 
        if linea.startswith("X-DSPAM-Confidence:"): 
            lstDatos.append(linea.split()[1]) 
            ct += 1   
except Exception as e:
    print("Error al leer el archivo" , e)

suma = calcularSpam(lstDatos,sumatorio)


promedio = calcularPromedio( suma, ct ) 

fd.close()     

print()
print("-"*15,"INFORME".center(10),"-"*15)
print(f"Archivo abierto: {nombre}") 
print("Las lineas con spam son: " , ct) 
print(f"El promedio de spam es de: {promedio} ") 




