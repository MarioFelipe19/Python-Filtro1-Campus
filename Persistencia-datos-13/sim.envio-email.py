fd = open("Persistencia-datos-13/mbox-short.txt" , "r") 

fd2 = open("Persistencia-datos-13/envio-emails.txt" , "w")

lstEmail = []

for linea in fd: 
    if linea.startswith("From:"):
        email = linea.split()[1]  
        if email not in lstEmail: 
            lstEmail.append(email)  


for i in range (len(lstEmail) -1, -1, -1):   #Revisa la lista al reves de abajo hacia arriva 
            
            #Enviar correo simulado
            msj = f"{lstEmail[i]} enviado [ok]" 
            print(msj)
            fd2.write(msj + "\n")

fd.close()
fd2.close()