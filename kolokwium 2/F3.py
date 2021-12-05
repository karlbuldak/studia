def f3(t):
    import re
    a=re.findall(r'\d+',t)
    return(min(a))

print(type(f3("78, 302 29; 14 - 69")))
print(type(f3("31-650; B17 => G777")))
