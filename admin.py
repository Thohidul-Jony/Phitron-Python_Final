from bank import Bank
from user import User


class Admin:
    def __init__(self, bank):
        self.__bank: Bank = bank

    def create_account(self, name, email, address, account_type) -> User:
        return self.__bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number) -> None:
        account = self.__bank.get_account(account_number)
        if account:
            del self.__bank.accounts[account_number]
            print(f"Account {account_number} has been deleted.")
        else:
            print("Account does not exist.")

    def list_all_accounts(self):
        return self.__bank.accounts

    def check_total_balance(self) -> int:
        total_balance = sum(user.balance for user in self.__bank.accounts.values())
        return total_balance

    def check_total_loan_amount(self) -> int:
        total_loan_amount = sum(
            account.loan for account in self.__bank.accounts.values()
        )
        return total_loan_amount