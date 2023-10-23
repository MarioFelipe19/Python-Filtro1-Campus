

periodicoIngles = int(input("Digite el numero de estudiantes que estan en el periodico de ingles "))
periodicoFrances = int(input("Digite el numero de estudiantes que estan en el periodico de frances ")) 

for i in range(1, periodicoIngles+1): 
    conjuntoIngles = set() 
    est = int(input("Digite el codigo del estudiante de ingles")) 
    conjuntoIngles.add(est)  
    print(conjuntoIngles)

for i in range(1 , periodicoFrances+1): 
    conjuntoFrances = set()
    est = int(input("Digite el codigo del estudiante frances")) 
    conjuntoFrances.add(est) 
    print(conjuntoFrances)


estInglesSolo = set(conjuntoIngles)- set(conjuntoFrances) 
print(f"Los estudiantes que estan solo en el periodico de ingles son: {len(estInglesSolo)} ")