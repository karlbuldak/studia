def f2(a1,a2):
    m=0
    n=0
    for i in a1:
        if i>9 and i<100:
            m+=1
    for j in a2:
        if j>9 and j<100:
            n+=1
    return(m==n)

    