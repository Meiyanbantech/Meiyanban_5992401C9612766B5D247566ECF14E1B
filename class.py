class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"

# Create an instance of the BankAccount class
my_account = BankAccount("123456789", "John Doe", 1000)

# Test deposit functionality
print(my_account.deposit(500))  # Deposited $500. New balance: $1500

# Test withdrawal functionality
print(my_account.withdraw(200))  # Withdrew $200. New balance: $1300

# Display the account balance
print(my_account.display_balance())  # Account balance for John Doe: $1300
