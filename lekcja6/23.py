import csv
with open('students.txt','r') as f:
    csvfile=csv.reader(f)
#     header=next(csvfile)
#     for i in csvfile:
#         if len(i[0])<8:
#             print(i[0],'\t\t',i[1],'\t\t',i[4])
#         else:
#             print(i[0],'\t',i[1],'\t\t',i[4])
    for a in csvfile:
        print(a)
#             

