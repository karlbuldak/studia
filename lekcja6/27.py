import re
for line in open('30linijek.txt'):
    for match in re.finditer('\b\w{6,}\b', line):
        print(line)
        