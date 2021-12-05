def f5(c):
    suma=0
    with open('poem.txt') as file:
        for i in file:
            if (c) in i or c.upper() in i:
                suma+=1
    return(suma)

print(f5('m'))
            

    
    