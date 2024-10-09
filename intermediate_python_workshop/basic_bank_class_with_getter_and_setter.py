# author: Dharm Vashisth
# date: 2024-10-10

class BankAccount:
    def __init__(self):
        self._balance = 0

    #  getter with the attribute name balance.
    #  As we have _balance in class, now we could access it using .balance also.
    @property
    def balance(self):
        return self._balance

    #  setter method with the attribute name i.e., balance.setter.
    #  As we have _balance in class, now we could set the value using balance=4 also.
    @balance.setter
    def balance(self, amount):
        self._balance=amount

    def deposit(self, amount):
        self._balance+=amount
    def withdraw(self,amount):
        if amount<self.balance:
            self._balance-=amount

def main():
    bank = BankAccount()
    bank.deposit(100)
    print("Deposited 100 in your bank account.")
    print("Balance:",bank.balance) # accessed by getter method
    # setting the value using setter method it is equivalent to bank._balance = 50
    bank.balance = 50
    print("New Balance:", bank.balance)  # accessed by getter method

if __name__=="__main__":
    main()