
def calcularPromedio(nota1 , nota2 , nota3): 


    promedio = nota1 * 0.30 + nota2  * 0.30 + nota3 *0.40 
    return promedio

lstEstudiantes = []
codigo = 0 


while codigo != 999: 
    print("\nDatos estudiante") 
    datEstudiante = {} 
    datEstudiante["codigo"]= int(input("Digite el codigo"))  
    datEstudiante["nombre"] = input("Nombre? ") 
    datEstudiante["nota1"] = float(input("Digite la 1ra nota: ")) 
    datEstudiante["nota2"] = float(input("Digite la 2da nota: ")) 
    datEstudiante["nota3"] = float(input("Digite la 3ra nota: "))

    datEstudiante["notaTotal"] = calcularPromedio(datEstudiante["nota1"],datEstudiante["nota2"] , datEstudiante["nota3"] ) 

    lstEstudiantes.append(datEstudiante) 
   
    
    print("*" *40)

    if datEstudiante["notaTotal"] <= 3.0:  
        print(f"El estudiante ha reprobado con{datEstudiante['notaTotal']}") 
    else: 
        print(f"El estudiante a aprobado con{datEstudiante['notaTotal']}")  

    print("\n\n" , "=" *30) 
    print("INFORME") 
    print("=" *30) 
    print("NOMBRE\t\tCodigo\t\tNOTAFINAL") 
    print("=" *30)  

    for i in range(len(lstEstudiantes)): 
        print(f"{lstEstudiantes[i]['nombre']}\t\t {lstEstudiantes[i]['codigo']}\t\t{lstEstudiantes[i]['notaTotal']}") 

    print("\n\n","=" *30) 

    

    codigo = int(input("Si desea continuar digite el codigo 999 sino digite otro codigo"))  


print("Muchas gracias pro usar el software")