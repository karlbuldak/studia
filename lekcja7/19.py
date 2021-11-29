import stack
expression=input('Input a RPN expression: ')
expression=list(expression)
for i in expression:    
    if i=='+' or i=='-' or i=='*' or i=='/':
        a=stack.pop()
        b=a
        c=stack.pop()
        if i=='+':
            stack.push(a+b)
        if i=='-':
            stack.push(a-c)
        if i=='*':
            stack.push(a*c)
        if i=='/':
            stack.push(a/c)
    if i=='=':
        d=stack.pop()
    else:
        stack.push(i)
        
print(d)
        


        