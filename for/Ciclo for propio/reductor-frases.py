frase = input("Frase? ") 
letra = input("Letra para acabar con el bucle? ") 

lstVocales = ["a" , "e" ,"i" , "o" ,"u"]

for l in frase: 
    if l.lower() == letra: 
        break 
    elif l.lower() in lstVocales: 
        continue #El continue ingnorara todo el codigo que esta debajo de el y seguira con la siguiente iteracion
    
    print(l, end="") 
print()