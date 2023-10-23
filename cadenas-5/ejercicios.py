num = input("Digite el numero de telefono: ")


if num.startswith("+") and num.count("-") ==  2: 
    partes = num.split("-") 
    print("El telefono es : " , partes[1]) 

else : 
    print("Error .El numero no cumple con el formarto") 



palabra = input("Ingrese una palabra palindrope: ") 

if (palabra == palabra[::-1]): 
    print("La palabra es palindrope ") 
else: 
    print("La palabra no es palindrope ") 
 


 # Escribir programa que pregunte al usuario fecha de nacimiento en formato dd/mm/aaaa

fecha = str(input("Digite la fecha de nacimiento en el siguiente formato dd/mm/aaaa: ")) 

partes = fecha.split("/") 

if partes[0].isdigit() and \
    partes[1].isdigit() and \
    partes[2].isdigit() and \
    (len(partes[0]) == 2 or len(partes[0]) == 1) and \
    (len(partes[1]) == 2 or len(partes[1]) == 1) and \
    len(partes[2]) == 4: 

    print(f"El día es {partes[0]}, el mes es {partes[1]}, el año es {partes[2]}")

else: 
    print("Formato incorrecto")








