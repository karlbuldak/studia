class Arrays():

    @staticmethod
    def ile(array, od, do):
        a=0
        for i in array:
            if i in range(od, do):
                a+=1
        return(a)

    @staticmethod
    def add_elements(number, value):
        list=[]
        for i in range(number):
            list.append(value)
        return(list)
    
    @staticmethod
    def random_elements(number, od, do):
        import random
        list=[]
        for i in range(number):
            list.append(random.randint(od,do))
        return(list)

    @staticmethod
    def print_all(array):
        for a in array:
            if a!=array[len(array)-1]:
                print(a, end=', ')
            else:
                print(a)

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
print(Arrays.add_elements(10,4))
print(Arrays.random_elements(20,-7,8))
print(Arrays.ile(Arrays.random_elements(20,-7,8),-1,1))


