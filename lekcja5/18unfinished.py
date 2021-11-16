def bubblesort(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            array[i]=array[i+1]
    return(array)
            
print(bubblesort([3,8,5,4,3,43]))
            