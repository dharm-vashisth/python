# list of numbers
items = [1,2,3,4,5,6]
for item in items:
    print(item)

# even numbers out of list using list comprehension
number = range(244)
even= [num for num in number if num%2==0]
print(even)

# dictionary containing number anf square of odd number from the list of numbers
square_even= {num:num**2 for num in number if num%2!=0}
print(square_even)
