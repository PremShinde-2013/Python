class BankAccount:

    BankName= "Prem bank"   # class attribute (shared)

    def __init__(self,owner,balance=0.0):
        self.balance = balance    # instance attributes (per object)
        self.owner = owner 
    
    def deposit(self,amount):
        self.balance += amount
        return  self.balance
    
    def statement(self):
        return f"The balance of {self.owner} at {BankAccount.BankName} is {self.balance:.2f} "
    
o1 = BankAccount("Prem",10000)

print(o1.statement())

o1.deposit(500)
print(o1.statement())

# Attributes = data on the object.
# Methods = functions that use that data.