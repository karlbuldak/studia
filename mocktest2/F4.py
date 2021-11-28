def f4(d):    
    suma=0
    for k,v in d.items():
        for i in v:
            if i>=5 and i<=10:
                suma+=i
    return(suma)
