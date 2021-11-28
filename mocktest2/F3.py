def f3(t):
    suma=0
    import re
    tablica=re.findall(r"\b\d{2,3}\b",t)
    for i in tablica:
        i=int(i)
        suma+=i
    return(suma)


    