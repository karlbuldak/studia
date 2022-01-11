class C():
    def __init__(self, string):
        self.string=string
    def m(self):
        strlist=[]
        for i in self.string:
            if i not in strlist:
                strlist.append(i)
        return(len(self.string)==len(strlist))

