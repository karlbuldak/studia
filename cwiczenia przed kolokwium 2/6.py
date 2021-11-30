def f6(lista):
    a=[]
    for i in lista:
        i=len(i)
        a.append(i)
    dlugas=max(a)
    return(lista[a.index(dlugas)])
    
    
print(f6(['ktory','wyraz','bedzie','najdluzszy', 'ten', 'a', 'możetenbedzienajdluzszy']))
