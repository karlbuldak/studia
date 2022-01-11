class C():
    def m(self,n1,n2):
        licznik=0
        import json
        with open('mockdata.json') as file:
            slownik=json.load(file)
            for i in range(len(slownik)):
                if slownik[i]["wife"]["age"]>=n1 and len(slownik[i]["children"])>=n2:
                    licznik+=1
        return(licznik)
    def m2(self, n1):
        rodziny=[]
        import json
        with open('mockdata.json') as file:
            slownik=json.load(file)
            for i in range(len(slownik)):
                if len(slownik[i]['children'])>=n1:
                    rodziny.append(slownik[i])
        with open('mockdata1.json', 'w') as file1:
            json.dump(rodziny,file1)
            

