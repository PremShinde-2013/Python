class SafeAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)  # underscore → “internal use”

    @property
    def balance(self):                  # read-only property (for now)
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = float(value)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

acc = SafeAccount("Aditi", 500)
acc.balance(600)
acc.deposit(200)
print(acc.balance)  # 700.0
# acc.balance = 0  # AttributeError if you add a setter later to prevent this
