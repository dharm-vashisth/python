class BankAccount:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount

def main():
    bank = BankAccount()
    bank.deposit(100)
    print("Deposited 100 in our bank")
    print("Balance:",bank.balance)

if __name__=="__main__":
    main()