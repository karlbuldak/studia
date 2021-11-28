import stack
stack.display()
a=[2,14,9]
for l in a:
    stack.push(l)
stack.display()
stack.pop()
stack.display()
b=[31,6]
for s in b:
    stack.push(s)
for i in range(2):
    stack.pop()
stack.display()