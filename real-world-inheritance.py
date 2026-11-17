#we are going to create a banking application that uses classes
#the base/parent class is going to be a bank account that has an owner and a balance as properties
#the child/derived class will be checkingaccount which will inherit from the bankaccount class but will have an overdraft property
#another child/derived class for savings account that will have a interest rate property
#they can all withdraw and deposit
#savings account will have an addition method to add interest

#base/parent class
#default a property value is propert=value
#this is a default parameter or property
class BankAccount:
    def __init__(self,owner,balance=0.0):
        self.owner = owner
        self.balance = balance

    #create a method for depositing money
    def deposit(self,amount):
        if amount <= 0:
            print("Deposits must be positive")
            return
        else:
            self.balance = self.balance + amount
            print(f"Your balance is now {self.balance}")

    #create method for withdraw
    def withdraw(self,amount):
        if amount <= 0:
            print("Withdraw amounts must be positive")
            return
        if amount > self.balance:
            print("Insufficent funds")
            return
        self.balance = self.balance - amount
        print(f"You balance is {self.balance}")

class CheckingAccount(BankAccount):
    #we can inherit all the things from bank account and even add additional properties
    def __init__(self,owner,balance=0.0,overdraft_limit=100.00):
        #if we add additional properties, we can tell the child/derived class to use the same constructor method as the base class
        #use the keyword super() to say hey use the same implementation of taking our owner and balance as BankAccount
        super().__init__(owner,balance)
        self.overdraft_limit = overdraft_limit

    #we can also override methods/functions for our checking account to check overdraft limit
    #we just name the function the same thing we do in the BankAccount, but change its implementation
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw must be positive")
            return
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawl exceeds overdraft limit")
            return
        self.balance = self.balance - amount
        print(f"Your balance is {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    #i dont need to change withdraw and deposit I need another new function/method for applying interest
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Your balance is {self.balance}")

myaccount = BankAccount("Zach Hamby",1000.00)
print(myaccount.balance)

myaccount.deposit(100.00)
print(myaccount.balance)

myaccount.withdraw(10000)
print(myaccount.balance)


print("*************************")
check_account = CheckingAccount("Aly Hamby", 500.00, 200.00)
check_account.deposit(200.00)
print(check_account.balance)

check_account.withdraw(850)
print(check_account.balance)

print("*****************************")

saving_acct = SavingsAccount("Trish",1500.00)
saving_acct.apply_interest()
print(saving_acct.balance)