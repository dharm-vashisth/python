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
    bank.deposit(100)
    print("Deposited 100 in our bank.")
    print(bank)
    bank.withdraw(10)
    print("Withdrawal of 10 from your bank.")
    print(bank)
    print(repr(bank)) # for debugging purpose

if __name__=="__main__":
    main()