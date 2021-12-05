def f5(x,y):
    a=[]
    slowo=[]
    zwrot=''
    zwrot=str(zwrot)
    with open('beautybeast.txt') as file:
        for line in file:
            a.append(line)
        wybranalinia=(a[y-1])
        lista=list(wybranalinia)
        for i in range(x):
            slowo.append(lista[i])
        for j in slowo:
            zwrot+=j
    return(zwrot)
