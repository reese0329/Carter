

#1
class BankAccount:
    def __init__(self,acct_number,acc_name):
        self.acct_number = acct_number
        self.acct_name = acc_name
        self.balance = 0.0

    def displayBalance(self):
        print ("The account balance is:",self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("You deposited", round(amount,2))
        print("The new balance is:",round(self.balance,2))

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("You withdrew", amount)
            print("The new balance is:",round(self.balance,2))
        else:
            print("You tried to withdraw", amount)
            print("The account balance is:",round(self.balance,2))
            print("Withdrawal denied. Not enough funds.")

myAccount = BankAccount(23456,"cici")
print("Account name:",myAccount.acct_name)
print("Account number:",myAccount.acct_number)
myAccount.displayBalance()

myAccount.deposit(34.52)
myAccount.withdraw(12.25)
myAccount.withdraw(30.18)

# 2
class InterestAccount(BankAccount):
    def __init__(self,acct_number,acct_name,rate):
        BankAccount.__init__(self,acct_number,acct_name)
        self.rate = rate

    def addInterest(self):
        interest = self.balance * self.rate
        print("adding interest to the account",self.rate*100,"percent")
        self.deposit(interest)


myAccount = InterestAccount(234567,"cici",0.11)
print("Account name:",myAccount.acct_name)
print("Account number:",myAccount.acct_number)
myAccount.displayBalance()
myAccount.deposit(34.52)
myAccount.addInterest()