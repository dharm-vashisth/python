# first line of python directory
print('Hello World', end="\n\n")

# Data Types in python:
'''
1. String
2. Number [int, float, complex]
3. Boolean
4. List
5. Tuple
6. Set 
7. Dictionary
'''

# String
data_type = 'String'
print(data_type)

_my_name = 'Python'
print("My name is {}. Nice to see you all here :)".format(_my_name), end="\n\n")

# Numbers
data_type = 'Numbers'
print(data_type)

lucky_number = 0
print(f"First Number discovered which helps in counting beyond single digit is {lucky_number}")

pi = 3.14
radius = 4
print(f"Area of circle with radius {radius}cm is {pi * radius ** 2}cm2")

complex_number = complex(23, 5)
print(f"Complex number is {complex_number}.")
print(f"Real number: {complex_number.real} and imaginary number is {complex_number.imag}", end="\n\n")

# Boolean
data_type = 'Boolean'
print(data_type)

number1 = 5
number2 = 7
print(f"{number1} is greater than {number2}? => {number1 > number2}")
print(f"{number1} is not greater than {number2}? => {number1 < number2}", end="\n\n")


##


# Custom Functions: buying movie ticket from wallet.
def purchase_tickets(wallet, expense):
    if wallet < expense:
        print("It is better to go for a walk as it is good for our health")

    else:
        wallet -= expense
        print("Hurray!! you have purchased 2 movie tickets. Enjoy the movie!!!")

    return wallet


def ticket_functionality(main_balance=1000):
    movie1 = float(input("Pls provide the price for movie ticket 1: "))
    movie2 = float(input("Pls provide the price for movie ticket 2: "))
    movie_expense = movie1 + movie2
    print("Doing the science....", end='\n\n')
    _balance = purchase_tickets(main_balance, movie_expense)
    return _balance


user_input = input("Press 1 to continue... ")
if user_input == '1':
    wallet_balance = ticket_functionality(2000)
    print(f"wallet_balance is {wallet_balance}")
