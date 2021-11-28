def f6(g,n1,n2):
    lista=[]
    file=open('people.csv',newline='')
    import csv
    reader=csv.reader(file)
    header=next(reader)
    for row in reader:
        height=int(row[2])
        if row[3]==g and height>=n1 and height<=n2:
            lista.append(row[0])
    return(len(lista))

print(f6('Female',160,180))
        

