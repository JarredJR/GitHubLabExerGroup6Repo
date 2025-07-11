from postlab.Bank import Bank 
from postlab.SavingsAccount import SavingsAccount  

def main():
    bank = Bank()

    num_accounts = int(input("Enter the number of accounts: "))

    for i in range(num_accounts):
        print(f"\nEnter details for Account {i + 1}:")
        name = input("  Account Holder Name: ")
        balance = float(input("  Balance: "))
        bank.add_account(SavingsAccount(name, balance))

    print("\nSorted Bank Accounts:")
    print(bank)

if __name__ == "__main__":
    main()
