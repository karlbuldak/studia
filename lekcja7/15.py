student={'name':'Karol',
         'surname':'Bułdak',
         'major':'CS',
         'uni':'UEK',
         'age':18,
         'passed':True,
         'average':4.30,
         'hobbies':['basketball','art','sports']
         }
import json
with open('student.json','w') as file:
    a=json.dumps(student,indent=4)
    for i in a:
        file.write(i)