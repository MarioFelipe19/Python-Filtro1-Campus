rows = int(input("Cantidad de filas ? "))
colums = int(input("Cantidad de columnas? ")) 

if rows == colums: 
    matrix = [] 

    for row_posicion in range(rows): 
        row = []

        for element in range(colums): 
            row.append(input(f"Digite un elemeneto a la fila {row_posicion}: "))
            
        matrix.append(row) 

    for row in matrix: 
        print(row) 

else: 
    print("La matriz debe ser cuadrada")