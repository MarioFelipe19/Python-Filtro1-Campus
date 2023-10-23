def miFun(email): 
    return len(email)

fd = open("Persistencia-datos-13/mbox-short.txt" , "r") 

setEmail = set()

for linea in fd: 
    if linea.startswith("To:"): 
        #cl += 1 
        #email = linea.split()[1] 
        #print(email) 
        setEmail.add(linea.split()[1])


fd.close()


cl = len(setEmail) 
print("La cantidad de correos de destino son: " , cl) 

"""
for email in sorted(setEmail , reverse=False , key=lambda x: len(x)): #Ordenar de mayor a menor devulve reverse = True , lamba ordena con la longitud de x que es el email
    print(email) 
"""

for email in sorted(setEmail , reverse=False ,  key = miFun ): 
    print(email , "Enviado")