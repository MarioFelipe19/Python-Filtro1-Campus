#Ejercicio 
#Hacer un programa que lea N esudiantes (nombre ,nota). Y nos muestre el promedio de la clase , el estudiante con mayor nota y el estudiante con meno nota. 



def leerInt(msj):
    while True:
        try:
            num = int(input(msj))
            if num < 1:
                print("Valor inválido. Debe ser mayor a cero")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...") 

def leerNota(msj):
    while True:
        try:
            num = float(input(msj))
            if num < 0:
                print("Nota inválido. Debe ser mayor o igual a cero")
                continue
            return num
        except ValueError:
            print("Error al ingresar el número.")
            input("Presione cualquier tecla para continuar...") 

def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

n = leerInt("Cuantos estudiantes son?") 

lstNombre=[] 
lstNotas=[] 
for i in range (1 , n+1): 
    print("\nDatos del estudiante # " , i) 
    lstNombre.append(leerNombre("Nombre?")) 
    lstNotas.append(leerNota("Nota?")) 

#Calcular y mostar el promedio 
prom = sum(lstNotas) / n 
print("\n" , "=" * 30) 
print("El promedio del curso es: " , prom) 

#Encontrar y mostrar el estudiante con mayor nota 
notaMayor = max(lstNotas) 
posEstMayor = lstNotas.index(notaMayor) #Nos da la posicion del estudiante que tiene la nota mayor 
nomEstMayoNota = lstNombre[posEstMayor] 
print("EL estudiante " , nomEstMayoNota , "tiene la mayor nota: " , notaMayor)


#Encontrar y mostrar el estudiante con menor nota  
notaMenor = min(lstNotas) 
posEstMenor = lstNotas.index(notaMenor) #Nos da la posicion del estudiante que tiene la nota mayor 
nomEstMenoNota = lstNombre[posEstMenor] 
print("EL estudiante " , nomEstMenoNota , "tiene la menor nota: " , notaMenor)