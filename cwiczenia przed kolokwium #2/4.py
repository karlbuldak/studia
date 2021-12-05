def f4(age):
    import json
    a=[]
    with open('students.json') as file:
        content=json.load(file)
        for n in range(100):
            if (content['students'][n]['age'])>age:
                a.append(content['students'][n]['name'])
        return(len(a))
        
print(f4(22))

            
   