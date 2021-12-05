def f7(n):
    a=0
    b=1
    if n==1:
        return(0)
    if n==2 or n==3:
        return(1)
    if n>3:
        while n>0:
            a=b
            b+=a
            n-=1
        return(a+b)
            
        
        