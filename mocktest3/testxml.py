import xml.etree.ElementTree as ET
tree=ET.parse('mockdata.xml')
root=tree.getroot()
dzieci=[]
strdzieci=''
for i in range(len(root)):
    for a in range(len(root[i][3])):
        dzieci.append(root[i][3][a].text)
        for b in dzieci:
            strdzieci+=f'{b} '
            dzieci=[]
    print(f'Family Number {i+1}: ' + root[i][1][0].text + ' ' + root[i][0].text + ' and ' + root[i][2][0].text + ' ' + root[i][0].text + ' and their children are ' + strdzieci)
    strdzieci=''
