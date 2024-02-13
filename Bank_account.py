class BankAccount:
    """
    Represents a simple bank account.

    Attributes:
    - account_number (int): The unique identifier for the bank account.
    - owner_name (str): The name of the account owner.
    - balance (float): The current balance in the account.

    Methods:
    - __init__(account_number, owner_name, initial_balance=0): Initializes a new BankAccount instance.
    - deposit(amount): Deposits the specified amount into the account.
    """

    def __init__(self, account_number, owner_name, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Parameters:
        - account_number (int): The unique identifier for the bank account.
        - owner_name (str): The name of the account owner.
        - initial_balance (float, optional): The initial balance in the account (default is 0).
        """
        self.ownername = owner_name
        self.balance = initial_balance
        self.account_number = account_number

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Parameters:
        - amount (float): The amount to be deposited.

        Note:
        - If the specified amount is greater than 0, it will be added to the account balance.
        - If the specified amount is not greater than 0, an "Invalid amount added" message will be printed.
        """
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount added")

    
    def withdrawal(self, amount):
        """
        Withdraws the specified amount from the bank account.

        Parameters:
        - amount (float): The amount to be withdrawn.

        Prints:
        - "Invalid withdrawal amount" if the amount is negative.
        - "Insufficient funds" if the withdrawal amount exceeds the current balance.
        - Otherwise, updates the balance by subtracting the withdrawal amount.

        Raises:
        - ValueError: If the amount is negative.
        """
        if amount < 0:
            print("Invalid withdrawal amount")
        elif amount >= self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        """
        Returns a string representation of the BankAccount.

        Returns:
        str: A formatted string containing account details - Account Number, Owner, and Balance.
        """
        return f"Account Number: {self.account_number} \nOwner: {self.ownername} \nBalance: {self.balance}"


# Example usage:

# Create a BankAccount instance
account = BankAccount("12345678", "John Doe")

# Deposit 1000.0 into the account
account.deposit(1000.0)

# Withdraw 500.0 from the account (successful)
account.withdrawal(500.0)

# Withdraw 600.0 from the account (insufficient funds)
account.withdrawal(600.0)

# Print the account details
print(account)   