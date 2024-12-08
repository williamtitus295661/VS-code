# Look at the following description of a problem domain: 
#   The bank offers the following types of accounts to its customers: savings accounts,
# checking accounts, and money market accounts. Customers are allowed to deposit
#  money into an account (thereby increasing its balance), withdraw money from an
#  account (thereby decreasing its balance), and earn interest on the account. Each
#  account has an interest rate.
#   Assume that you are writing a program that will calculate the amount of interest
# earned for a bank account.
#   Identify the potential classes in this problem domain.
#   Refine the list to include only the necessary class or classes for this problem.
#   Identify the responsibilities of the class or classes.

class Account:
    def __init__(self, balance, intrest_rate):
        self.balance = balance
        self.intrest_rate = intrest_rate

    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def intrest_rate(self):
        return self._intrest_rate
    @intrest_rate.setter
    def intrest_rate(self, value):
        self._intrest_rate = value

    def deposit(self, amount):
        self.balance += amount

    def witdraw(self, amount):
        self.balance -= amount

    def accrue_intrest(self):
        self.balance *= 1  + self.intrest_rate / 100
my_account = Account(100, 3)
my_account.accrue_intrest()
print(my_account.balance)
my_account.witdraw(100)
print(my_account.balance)
my_account.deposit(100)
print(my_account.balance)


            

    
   
    


