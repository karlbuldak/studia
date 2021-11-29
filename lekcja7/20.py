import json
students=open('students.json','r')
a=json.load(students)
for i in a:
    del i['gender']
    del i['age']
    del i['year_of_study']
    del i['email']
formated=open('limited.json','w')
json.dump(a, formated)
formated.close()
students.close()

