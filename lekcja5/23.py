def median(array):
    posortowana=sorted(array)
    if len(array)%2==0:
        b=posortowana[len(posortowana)//2]
        c=posortowana[len(posortowana)//2-1]
        print((b+c)/2)
    if len(array)%2==1:
        b=posortowana[len(posortowana)//2]
        print(b)
        
print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))

        