import csv
lista=[]
lista2=[]
with open('workers.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)
    for i in csv_reader:
        slownik={
        'name'i:(i[0]),
        'age'i:(i[3])
        }
print(slownik)
        


        
    