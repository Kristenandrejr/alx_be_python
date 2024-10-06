class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an optional starting balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds are available. Return True if successful, otherwise False."""
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")
