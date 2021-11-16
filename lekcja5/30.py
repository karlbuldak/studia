def rand_elem(array):
    import random
    return(array[random.randint(0, len(array)-1)])
    
print(rand_elem([1,2,3,4,5,6]))