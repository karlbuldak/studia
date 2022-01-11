class C():
    @staticmethod
    def m(n1, n2):
        a=0
        import xml.etree.ElementTree as ET
        tree = ET.parse('mockdata.xml')
        root=tree.getroot()
        for i in range(len(root)):
            if len(root[i][3])>=n2 and int(root[i][2][1].text)>=n1:
                a+=1
        return(a)
                

print(C.m(60,1))
    
