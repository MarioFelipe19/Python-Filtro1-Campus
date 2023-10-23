
#Invertir una cadena con un for

string = input("Digite la frase: ") 

stringInvertido = ""

for c in string : 
    stringInvertido = c + stringInvertido 

print(f"String invertido: {stringInvertido} ")