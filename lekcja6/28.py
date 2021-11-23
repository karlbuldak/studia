import re
file=open('grades.txt')
for i in file:
    a=(re.findall('\d.\d', i))
sum=0
for dig in a:
    dig=float(dig)
    sum+=dig
print(round(sum/len(a),2))