import time 

comienzo = time.time() 
print("Escribe algo")
input("") 
fin = time.time() 
print(f"{fin-comienzo:.1f}")