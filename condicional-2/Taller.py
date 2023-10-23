print("Punto 1")
print("*")
print("**")
print("***")
print("****") 

print("Punto 2")
print("******")
print("*    *") 
print("*    *") 
print("*    *") 
print("******") 


print("Punto 3")

valorHora = 20000 

horasTrabajadas = int(input("Digite las horas trabajadas:"))

salarioBruto = valorHora * horasTrabajadas 

print("Su sueldo bruto es: ${:,} ".format(salarioBruto))

descuentoEps = salarioBruto * 0.04  

print("Descuento de afiliacion a EPS: ${:,}" .format(descuentoEps))

descuentoPension = salarioBruto * 0.04

print("Descuento de pension: ${:,} " .format(descuentoPension))

descuentosTotales = descuentoEps + descuentoPension

print("Salario neto: ${:,}" .format(salarioBruto - descuentosTotales) )    


#Conversor de segundos 
print("Punto 4") 


entradaSegundo = int(input("Digite los segundos a convertir: "))  

horas = entradaSegundo//3600  
sobrante1 = entradaSegundo%3600

minutos = sobrante1//60  
segundos = sobrante1%60 

print("Horas: " , horas) 
print("Minutos: " , minutos) 
print("Segundos" , segundos) 


#Curva 8
print("Punto 5") 

nota = float(input("Digite la nota de 0 a 5:")) 
curva = (nota*0.8) +1
print("La curva 8 equivale a: " , curva) 
