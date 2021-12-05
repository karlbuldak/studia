def f4(d,b):
    suman=0
    sumap=0
    if b==True:
        for k,v in d.items():
            if v%2==0:
                suman+=v
        return(suman)
    if b==False:
        for key,value in d.items():
            if value%2==1:
                sumap+=value
        return(sumap)
    
        