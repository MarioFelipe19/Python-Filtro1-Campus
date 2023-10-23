#Lanzar 100 veces un dado e imprimir cuantas veces cae el numero 5. 

import random 
cae5 = 0 #Variable tipo contador

for i in range(100): 
    dado = random.randrange(1,7)  

    if dado == 5: 
        cae5 += 1  
print(f"El lado 5 cayo: {cae5} veces ")