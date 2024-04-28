from typing import Union, Dict

class Bank:
    def __init__(self, initial_balance: int, loan_available: bool = True):
        self.accounts: Dict[str, User] = {}
        self.__available_balance = initial_balance
        self.__total_loan = 0
        self.__loan_available = loan_available

    def create_account(self, name: str, email: str, address: str, account_type: str) -> Union['User', str]:
        account_number = str(len(self.accounts) + 1)
        user = User(name, email, address, account_type, account_number)
        self.accounts[account_number] = user
        return user, account_number

    def get_account(self, account_number: str) -> Union['User', None]:
        return self.accounts.get(account_number)

    @property
    def available_balance(self) -> int:
        return self.__available_balance


class Admin:
    def __init__(self, bank: Bank):
        self.__bank = bank

    def create_account(self, name: str, email: str, address: str, account_type: str) -> Union['User', str]:
        return self.__bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number: str) -> None:
        account = self.__bank.get_account(account_number)
        if account:
            del self.__bank.accounts[account_number]

    def list_all_accounts(self) -> Dict[str, 'User']:
        return self.__bank.accounts

    def check_total_balance(self) -> int:
        total_balance = sum(user.balance for user in self.__bank.accounts.values())
        return total_balance

    def check_total_loan_amount(self) -> int:
        total_loan_amount = sum(account.loan for account in self.__bank.accounts.values())
        return total_loan_amount


class User:
    def __init__(self, name: str, email: str, address: str, account_type: str, account_number: str):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type
        self.__account_number = account_number

        self.__balance = 0
        self.__transactions = []
        self.__loan_taken = 0
        self.__loans = 0

    def __make_transaction(self, type: str, amount: int) -> str:
        return f"{type} {amount}TK"

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(self.__make_transaction("deposit", amount))

    def withdraw(self, amount: int) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(self.__make_transaction("withdraw", amount))

    def request_for_loan(self, amount: int) -> None:
        if self.__loan_taken < 2:
            if amount > 0 and amount <= self.__balance:
                self.__balance += amount
                self.__loan_taken += 1
                self.__loans += amount
                self.__transactions.append(self.__make_transaction("loan", amount))

    def balance_transfer(self, amount: int, acc) -> None:
        if acc:
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                self.__transactions.append(self.__make_transaction("transfer", amount))
                acc.deposit(amount)

    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def loan(self) -> int:
        return self.__loans

    @property
    def transactions(self) -> list:
        return self.__transactions


if __name__ == "__main__":
    bank = Bank(10000, True)
    admin = Admin(bank)
    users = {}
    user, account_number = bank.create_account("name", "email", "address", "account_type")
    users[account_number] = user
    users[account_number].deposit(1000)

    while True:
        print("Welcome!!")
        print("1. User")
        print("2. Admin")
        print("3. Exit")

        choice = int(input("Enter your option: "))
        if choice == 1:
            print("Welcome!!")
            print("1. Check balance")
            print("2. Check transaction history")
            print("3. Take loan")
            print("4. Transfer amount")
            print("5. Deposit")
            print("6. Withdraw")
            print("7. Exit")
            choice1 = int(input("Enter your option: "))
            if choice1 == 1:
                acc_num = input("Enter user account number: ")
                user = users.get(acc_num)
                if user:
                    print(user.balance)
                else:
                    print("Account not found")
            elif choice1 == 2:
                acc_num = input("Enter user account number: ")
                user = users.get(acc_num)
                if user:
                    print(user.transactions)
                else:
                    print("Account not found")
            elif choice1 == 3:
                acc_num = input("Enter user account number: ")
                user = users.get(acc_num)
                if user:
                    amount = int(input("Enter amount: "))
                    user.request_for_loan(amount)
                else:
                    print("Account not found")
            elif choice1 == 4:
                acc_num = input("Enter user account number: ")
                user = users.get(acc_num)
                if user:
                    rec_num = input("Enter recipient account number: ")
                    rec_user = users.get(rec_num)
                    if rec_user:
                        amount = int(input("Enter amount: "))
                        user.balance_transfer(amount, rec_user)
                    else:
                        print("Recipient account not found")
                else:
                    print("Account not found")
            elif choice1 == 5:
                acc_num = input("Enter user account number: ")
                user = users.get(acc_num)
                if user:
                    amount = int(input("Enter amount: "))
                    user.deposit(amount)
                else:
                    print("Account not found")
            elif choice1 == 6:
                acc_num = input("Enter user account number: ")
                user = users.get(acc_num)
                if user:
                    amount = int(input("Enter amount: "))
                    user.withdraw(amount)
                else:
                    print("Account not found")
            elif choice1 == 7:
                break
            else:
                print("Invalid option")
        elif choice == 2:
            print("Welcome!!")
            print("1. Create account for user")
            print("2. View all user accounts")
            print("3. Check total available balance")
            print("4. Check total loan amount")
            print("5. Delete user's account")
            print("6. Exit")
            choice1 = int(input("Enter your option: "))
            if choice1 == 1:
                name = input("Enter a name: ")
                email = input("Enter a email: ")
                address = input("Enter a address: ")
                account_type = input("Enter a account type: ")
                user, account_number = admin.create_account(name, email, address, account_type)
                users[account_number] = user
            elif choice1 == 2:
                for account_number, user in users.items():
                    print(f"Account {account_number}")
            elif choice1 == 3:
                total_balance = sum(user.balance for user in users.values())
                print(f"Total Balance in the Bank: {total_balance}TK")
            elif choice1 == 4:
                total_loan_amount = sum(user.loan for user in users.values())
                print(f"Total Loan Amount in the Bank: {total_loan_amount}TK")
            elif choice1 == 5:
                acc_num = input("Enter user account number: ")
                user = users.get(acc_num)
                if user:
                    admin.delete_account(acc_num)
                    del users[acc_num]
                    print(f"Account {acc_num} has been deleted.")
                else:
                    print("Account not found")
            elif choice1 == 6:
                break
            else:
                print("Invalid option")
        elif choice == 3:
            break
