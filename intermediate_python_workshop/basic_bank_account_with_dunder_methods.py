# author: Dharm Vashisth

class BankAccount:
    # dunder method
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount

    # dunder method
    def __str__(self):
        return f"Balance is {self.balance}"

    # dunder method
    def __repr__(self):
        return f"BalanceAccount (balance: {self.balance})"


def main():
    bank = BankAccount()
    bank.name = 'Ramo' # custom attribute for our object
    print("Welcome to our Reputed AB bank:", end='\n\n')
    bank.deposit(100)
    print(f"Dear {bank.name}, Deposited 100 in your bank account.")
    print(bank)
    bank.withdraw(10)
    print(f"Dear {bank.name}, Withdrawal of 10 from your bank account.")
    print(bank, end='\n\n')
    print("Ignore this line. Debugging stuff: ",repr(bank)) # for debugging purpose

if __name__=="__main__":
    main()