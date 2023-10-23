#Condicional simple 
#Calcular el sueldo de un empleado y darle auxTranporte si su sueldo es menor al min

sueldo = 1_000_000 
sueldoMin = 1_160_000 

if sueldo <= sueldoMin :
    auxTrans = 140_000 
else: 
    auxTrans = 0 

#F-string
print(f"Auxilio de transporte $ {auxTrans:,}") 
#.Format
print("Auxili de transporte $ {:,}".format(auxTrans)) 







