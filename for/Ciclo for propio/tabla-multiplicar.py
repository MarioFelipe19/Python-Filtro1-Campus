num = int(input("Digite un numero")) 

print(f"La tabla del {num} es : ")

for n in range(0 , 11): 
    mult = num*n
    print(f"{num} x {n} : {mult}")