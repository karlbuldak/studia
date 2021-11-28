def rand(od,do):
    import random
    x=random.randint(od, do)
    while x%6 != 0:
        x=random.randint(od, do)
    return(x)
    
print(rand(9,901))


