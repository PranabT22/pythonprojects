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
