from admin import Admin
from bank import Bank


def account_list(users):
    if len(users) > 0:
        for acc_num in users:
            print(f"Account {acc_num}")
    else:
        print("Account not found")


def create_account(bank: Bank):
    name: str = input("Enter a name : ")
    email: str = input("Enter a email : ")
    address: str = input("Enter a address : ")
    account_type: str = input("Enter a account type : ")
    return bank.create_account(name, email, address, account_type)


def deposit(users):
    acc_num: str = input("Enter user account number : ")
    amount: str = int(input("Enter amount : "))
    if acc_num in users:
        users[acc_num].deposit(amount)
    else:
        print("Account not found")


def withdraw(users, bank: Bank):
    acc_num: str = input("Enter user account number : ")
    amount: str = int(input("Enter amount : "))
    if bank.available_balance > amount:
        if acc_num in users:
            users[acc_num].withdraw(amount)
        else:
            print("Account not found")
    else:
        print("The bank is bankrupt")


def request_for_loan(users):
    acc_num: str = input("Enter user account number : ")
    amount: str = int(input("Enter amount : "))
    if acc_num in users:
        users[acc_num].request_for_loan(amount)
    else:
        print("Account not found")


def balance_transfer(users):
    acc_num: str = input("Enter user account number : ")
    rec_num: str = input("Enter recipient account number : ")
    amount: str = int(input("Enter amount : "))
    if acc_num in users and rec_num in users:
        users[acc_num].balance_transfer(amount, users[rec_num])
    else:
        print("Account not found")


def delete_account(users, admin: Admin):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        admin.delete_account(acc_num)
        del users[acc_num]
    else:
        print("Account not found")


def check_balance(users):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        print(users[acc_num].balance)
    else:
        print("Account not found")


def check_transactions(users):
    acc_num: str = input("Enter user account number : ")

    if acc_num in users:
        print(users[acc_num].transactions)
    else:
        print("Account not found")


def check_total_balance(admin: Admin):
    total_balance = admin.check_total_balance()
    print(f"Total Balance in the Bank: {total_balance}TK")


def check_total_loan_amount(admin: Admin):
    total_loan_amount = admin.check_total_loan_amount()
    print(f"Total Loan Amount in the Bank: {total_loan_amount}TK")


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
            check_balance(users)
        elif choice1 == 2:
            check_transactions(users)
        elif choice1 == 3:
            request_for_loan(users)
        elif choice1 == 4:
            balance_transfer(users)
        elif choice1 == 5:
            deposit(users)
        elif choice1 == 6:
            withdraw(users, bank)
        elif choice1 == 7:
            break
        else:
            print("Invalid option")
    elif choice == 2:
        print(f"Welcome!!")
        print("1. Create account for user")
        print("2. View all user accounts")
        print("3. Check total available balance")
        print("4. Check total loan amount")
        print("5. Delete user's account")
        print("6. Exit")
        choice1 = int(input("Enter your option: "))
        if choice1 == 1:
            user, account_number = create_account(bank)
            users[account_number] = user
        elif choice1 == 2:
            account_list(users)
        elif choice1 == 3:
            check_total_balance(admin)
        elif choice1 == 4:
            check_total_loan_amount(admin)
        elif choice1 == 5:
            delete_account(users, admin)
        elif choice1 == 6:
            break
        else:
            print("Invalid option")
    elif choice == 3:
        break
