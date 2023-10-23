#Condicional anidado   
#Sacar la nota de un estudiante y clasificarla del 0 al 100

nombre = input("Digite el nombre del estudiante: ")
notaCualitativa = int(input("Digite la nota [0-100]: "))  
nota = ""

if notaCualitativa >= 0 and notaCualitativa <= 59 : 
    nota = "D" 

elif notaCualitativa >= 60 and notaCualitativa <= 79 : 
    nota = "C" 

elif notaCualitativa >= 80 and notaCualitativa <= 89: 
    nota = "B" 

elif notaCualitativa >= 90 and notaCualitativa <= 100: 
    nota = "A" 

else: 
    nota = "" 
    print("Error nota invalida") 


print("\n" ,"-" *50)
print("Estudiante: " , nombre , "\nNota cuantitativa:" , notaCualitativa , "\nNota Cualitativa:" , nota ) 