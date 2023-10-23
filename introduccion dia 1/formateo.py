#Formatear la salida de datos

#CON FORMAT 
sueldo = 5600000 
print(" Sueldo: ${:,}".format(sueldo))

interes = 2568.3454353453 
print("Interes: ${:.3f}".format(interes)) 

# f-string 
print(f"sueldo: ${sueldo:,}")
print(f"Intereses: ${interes:,.3f}")