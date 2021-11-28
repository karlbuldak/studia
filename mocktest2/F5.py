def f5(c):
    suma=0
    file=open('poem.txt')
    for i in file:
        if (c) in i or c.upper() in i:
            suma+=1
    file.close()
    return(suma)

print(f5('m'))
            

    
    