import json
result=[]
with open('students.json') as f, open('formated2.json','w') as f2:
    data=json.load(f)
    for i in range(len(data)):
        dict={
    'firstname':data[i]['first_name'],
    'lastname':data[i]['last_name'],
    'email':data[i]['email']
                }
        result.append(dict)
    json.dump(result,f2,indent=4)

       
    