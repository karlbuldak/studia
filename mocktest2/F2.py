def f2(a1,a2):
    n=0
    m=0
    for i in a1:
        i=str(i)
        if len(i)==2:
            n+=1
    for j in a2:
        j=str(j)
        if len(j)==2:
            m+=1
    return(m==n)

print(f2([23,7,16,34],[1,18,79,20,6,111]))