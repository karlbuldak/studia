def sum(array):
    suma=0
    for i in array:
        suma+=i
    return(suma)

def array2str(array):
    strarray=''
    for i in array:
        strarray+=str(f'{i} ')
    return(strarray)
        
    
print(sum([4,5,3,2,4]))
print(array2str([8,9,10]))
        

    