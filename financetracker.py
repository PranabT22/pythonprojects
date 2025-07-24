class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
        else:
            raise TypeError("Expected an Account instance")

    def total_balance(self):
        return sum(account.balance for account in self.accounts)
        
class Account:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            raise TypeError("Expected a Transaction instance")
        
        self.transactions.append(transaction)

        # Update the balance
        if transaction.is_expense:
            self.balance -= transaction.amount
        elif transaction.is_income:
            self.balance += transaction.amount

    def check_balance(self):
        return f"Current balance for {self.name}: {self.balance}"

class Transaction:
    def __init__(self, amount, date, description, category, is_expense=False, is_income=False):
        if is_expense and is_income:
            raise ValueError("Transaction can't be both income and expense.")
        if not is_expense and not is_income:
            raise ValueError("Transaction must be either income or expense.")

        self.amount = amount
        self.date = date
        self.description = description
        self.category = category
        self.is_expense = is_expense
        self.is_income = is_income

    def check_transaction(self):
        if self.is_expense:
            return f"{self.amount} is an Expense"
        elif self.is_income:
            return f"{self.amount} is an Income"


# Creating a user
user = User("john_doe", "john@example.com")

# Creating an account
account = Account("Checking Account", 1000.0)
user.add_account(account)

# Creating a transaction
t1 = Transaction(amount=200, date=datetime.now(), description="Salary", category="Job", is_income=True)
t2 = Transaction(amount=50, date=datetime.now(), description="Groceries", category="Food", is_expense=True)

# Addition of transactions
account.add_transaction(t1)
account.add_transaction(t2)

# Checking the balance
print(account.check_balance())      
print(user.total_balance())   
