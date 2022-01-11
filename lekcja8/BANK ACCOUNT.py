class BankAccount():
    def __init__(self, number):
        self.number=number
        self.balance=0
    
    def status(self):
        print('Bank Account No: ', self.number)
        print(f'Balance: PLN {self.balance:.2f}')
        print()
        
    def deposit(self, amount):
        amount=float(amount)
        self.balance+=amount
        
    def withdraw(self, amount):
        amount=float(amount)
        if amount>=self.balance:
            print('Not enough funds on your bank account')
            print()
        else:
            self.balance-=amount
            
object=BankAccount('12 3456 5555 9090 1111 0000 7722')
object.status()
object.deposit(25.30)
object.status()
object.withdraw(31.72)
object.status()
object.withdraw(14.02)
object.status()