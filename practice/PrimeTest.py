for i in range ( 2,101):
    is_Prime = True
    for j in range ( 2, int ( i **0.5) +1):
        if i %j == 0:
            is_Prime = False
        if is_Prime:
            print(i, "is prime")
        else:
            continue