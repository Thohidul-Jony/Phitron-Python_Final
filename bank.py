from user import User


class Bank:
    def __init__(self, initial_balance, loan_available=True):
        self.accounts: dict[str, User] = {}
        self.__available_balance = initial_balance
        self.__total_loan = 0
        self.__loan_available = loan_available

    def create_account(self, name, email, address, account_type):
        account_number = str(len(self.accounts) + 1)
        user = User(name, email, address, account_type, account_number)
        self.accounts[account_number] = user
        print(f"Account created successfully for {name}. \nAccount number: {account_number}")
        return user, account_number

    def get_account(self, account_number) -> User:
        return self.accounts.get(account_number)

    @property
    def available_balance(self):
        return self.__available_balance