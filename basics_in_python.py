# first line of python directory
print('Hello World')


# buying movie ticket from wallet.
def purchase_tickets(wallet, expense):
    if wallet < expense:
        print("It is better to go for a walk as it is good for our health")

    else:
        wallet -= expense
        print("Hurray!! you have purchased two movie tickets. Enjoy the movie!!!")

    print(f"Wallet Balance: {round(wallet, 4)}")
    return wallet


wallet_balance = 1000 # 1000 inr
movie1 = float(input("Pls provide the price for movie ticket 1: "))
movie2 = float(input("Pls provide the price for movie ticket 2: "))
movie_expense = movie1 + movie2
print("Doing the science....")
wallet_balance = purchase_tickets(wallet_balance, movie_expense)
