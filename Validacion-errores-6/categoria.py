while True : 
    try:
        cat = int(input("Digite una categoria 1 , 2 o 3: ")) 
        if cat < 1 or cat > 3: 
            print("Categoria invalida. Ingrese 1 o 2 o 3 ") 
            continue #Vuelva a empezar el while  
        break 
    except ValueError: 
        print(" Error. Categoria invalida.")

