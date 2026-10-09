class BankAccount:
    def __init__(self,name,balance,acc):
        self.name=name
        self.balance=balance
        self.acc=acc
        
    def display(self):
        print("Account Holder Name : ",self.name)
        print("Balance : ",self.balance)
        print("Account No. : ",self.acc)

    def deposit(self,amount):
        self.balance+=amount
        print("Current balance: ",self.balance)

    def withdraw(self,draw):
        if draw<self.balance:
            self.balance-=draw
            print("withdrawl : ",draw)
            print("Balance after withdrawl : ",self.balance)
        else:
            print("Insufficiant funds")

    def transfer(self,transfer,other_account):
            if transfer<self.balance:
                self.balance-=transfer
                other_account.balance+=transfer
                print("Transfer amount : ",transfer)
                print("Balance after transfer : ",self.balance)
            else:
                print("Insufficiant funds")

s1=BankAccount("Dhairyasheel",0,3001)
s1.display()  
s1.deposit(10000)
s1.withdraw(2000)


print("\n")

s2=BankAccount("Vivek",0,3002)
s2.display()  
s2.deposit(50000)
s2.withdraw(1000)

print("\n")

s1.transfer(500,s2)
