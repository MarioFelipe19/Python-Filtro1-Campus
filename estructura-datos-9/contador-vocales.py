letras = []
while True: 
    letra = input("Ingrese una letra del abecedario : ") 

    if not letra.isalpha():  
        print("Error. Letra no valida\n") 
        input("Oprima entres para continuar")
        continue 

    letras.append(letra) 

    op = input("\n Desea continuar (s/n)?") 
    if op.lower() != "s" :
        break

print("\n" , "=" *30) 
vocales = ["a" , "e" , "i" , "o" , "u"] 
canVocales = [0] * 5

#Recorrer la lista por elemento 
for l in letras: 
    if l.lower() in vocales: #In es dentro , en cierta cosa
        p = vocales.index(l.lower()) #Busca la vocal y me devulve la posicion 
        canVocales[p] += 1 


#Recorrido por posicion       
for p in range(len(vocales)):#devulve la longitud de vocales = 5
    print(vocales[p] , "=" ,  canVocales[p])