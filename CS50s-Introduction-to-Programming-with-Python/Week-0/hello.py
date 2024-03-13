# How to print a message using the print function.

"""
print("Hello, World")
"""

# How to prompt a user response using the input function.

"""
print("What's your name? ")
input()
"""

# In python it is possible to print a line using the input function while at the same time giving the user the possibility to reply with a respone.

"""
input("What's your name? ")
"""

# Using variables we can make the program return a value.

"""
name = input("What's your name? ")
print("Hello, " + name + "!")
"""

# To simplify the code we can also remove the "+" and instead use "," to remove the need for manual spaces.

"""
name = input("What's your name? ")
print("Hello,",name + "!")
"""

# The print function has default parameters which are not visible but using the documentation(https://docs.python.org/3/library/functions.html#print) we can see which parameters are available and also how to edit them.

## In the example below I change the defualt parameter ("end=\n") of how the print funtion would end and begin on a new line.

"""
name = input("What's your name? ")
print("Hello, ", end="")
print(name)
"""

## In this example I change the default parameter for separators (sep=" ") which states that all spaces are separators to use underlines ("_") instead.

"""
name = input("What's your name? ")
print("Hello,", name, sep="_")
"""

# How to use quotation marks inside quotations (""Hello""), using an escape charachter ("\").

"""
print("Hello, \"friend\"")
"""

# To be able to format a string we can use string-methods {'string'} (https://docs.python.org/3/library/stdtypes.html#string-methods).
"""
name = input("What's your name? ")
print(f"Hello, {name}"+"!")
"""

## Remove eventual whitespaces(when user has hit space on accident, only removes whitespaces on the left or right) from str ( name(str).strip(method/function)).
"""
name = input("What's your name? ")
name = name.strip()
print(f"Hello, {name}"+"!")
"""

## Capitalize users name either by using .capitalize(Only capitalizes the first letter) or .title(Capitalizes first letter of every word).
"""
name = input("What's your name? ")
name = name.strip()
name = name.title()
print(f"Hello, {name}"+"!")
"""

## Chaining methods to clean code.
"""
name = input("What's your name? ")
name = name.strip().title()
print(f"Hello, {name}"+"!")
"""

## Chaining methods to the variable for the most effective and clean code.
"""
name = input("What's your name? ").strip().title()
print(f"Hello, {name}"+"!")
"""

## Split users name into first name and last name.
"""
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"Hello, {first}"+"!")
"""

