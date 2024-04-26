class User:
    def __init__(self, name, email, address, account_type, account_number):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__account_type = account_type
        self.__account_number = account_number

        self.__balance = 0
        self.__transactions = []
        self.__loan_taken = 0
        self.__loans = 0

    def __make_transaction(self, type: str, amount: str) -> str:
        return f"{type} {amount}TK"

    def deposit(self, amount: float | int) -> None:
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(self.__make_transaction("deposit", amount))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount: float | int) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(self.__make_transaction("withdraw", amount))
        else:
            print("Withdrawal amount exceeded")

    def request_for_loan(self, amount: float | int) -> None:
        if self.__loan_taken < 2:
            if amount > 0 and amount <= self.__balance:
                self.__balance += amount
                self.__loan_taken += 1
                self.__loans += amount
                self.__transactions.append(self.__make_transaction("loan", amount))
            else:
                print("Loan amount exceeded")
        else:
            print(
                f"You've reached the maximum number of allowed loans ({self.__loan_taken})."
            )

    def balance_transfer(self, amount: float | int, acc) -> None:
        print(acc)
        if acc:
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                self.__transactions.append(self.__make_transaction("transfer", amount))
                acc.deposit(amount)
            else:
                print("Invalid transfer amount.")
        else:
            print("Account does not exist.")

    @property
    def balance(self) -> int:
        return self.__balance

    @property
    def loan(self) -> int:
        return self.__loans

    @property
    def transactions(self) -> int:
        return self.__transactions

    @property
    def accounts(self):
        return self.__accounts