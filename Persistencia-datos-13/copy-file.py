fd = open("Persistencia-datos-13/nombres.txt" , "r")  

fd2 = open("Persistencia-datos-13/nombres-bak.txt" , "w")  

for linea in fd: 
    fd2.write(linea)


fd2.close()
fd.close()

print("Prodeco terminado")