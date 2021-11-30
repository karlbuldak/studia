def f6(g,n1,n2):
    a=0
    file=open('people.csv')
    import csv
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        height=int(row[2])
        if row[3]==g and height>=n1 and height<=n2:
            a+=1
    return(a)

print(f6('Female',160,180))
        

