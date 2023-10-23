#capturar las notas de un curso y calcular el promedio d estas.

#Mostrar en pantalla el resultado del promedio 


cant = int(input("Cual es la cantidad de notas: ")) 

sumaNotas = 0

for i in range( 1, cant + 1):  
    nota = float(input(f"Ingresa la nota:# {i}: "  )) 
    sumaNotas = sumaNotas + nota  

prom = sumaNotas / cant

print(f"El promedio de las notas es: {prom:.1f} " )