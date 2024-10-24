class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0  # Initialize the balance to 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}.")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}.")

def main():
    # Create a bank account instance
    account_number = input("Enter your account number: ")
    account = BankAccount(account_number)

    while True:
        print("\nChoose an option:")
        print("(a) Deposit money")
        print("(b) Withdraw money")
        print("(c) Check balance")
        print("(d) Exit")
        
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'a':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 'b':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 'c':
            account.check_balance()
        elif choice == 'd':
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the main function
main()