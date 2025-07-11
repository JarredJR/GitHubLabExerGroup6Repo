class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        sorted_accounts = sorted(self.accounts)  # Sort by name
        return "\n".join(str(account) for account in sorted_accounts)
