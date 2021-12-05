def f6(n1,n2,c):
    licznik=0
    lista=[]
    import csv
    with open('workers.csv','r') as file:
        data=csv.reader(file)
        header=next(data)
        for i in data:
            lista.append(i)
        for j in range(len(lista)):
            if int(lista[j][9])>=n1 and int(lista[j][9])<=n2 and lista[j][13]==c:
                licznik+=1
    return(licznik)


                    
