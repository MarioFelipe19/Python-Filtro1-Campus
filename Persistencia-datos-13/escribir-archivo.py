archivo = open("Persistencia-datos-12/salas.txt" , "w") 


archivo.write("sputnik\n\t")
archivo.write("apolo\n")
archivo.writelines(["houston\n" , "artemis\n"]) 

archivo.close()