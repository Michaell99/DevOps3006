import random

# Question A:

x = 2
y = 1

if x > y:
    print("BIG")
else:
    print("small")

# question B
z = 1
while z < 6:
    print(z)
    z = z + 1

# question C
d = random.randint(1, 5)
if d == 2:
    print(" winter")
elif d == 1:
    print("summer")
elif d == 3:
    print("fall")
elif d == 4:
    print("spring")

# question d the following loop will run 10 times and 10 will be printed last


# F
phone_number = str(input("What is you phone number? "))
print(f"You phone number is ", {phone_number})

# e

age = 22
first_letter = "M"
currency = 0.29
fly = False
apartment_number = 8

print(f'{age}, {first_letter}, {currency}, {fly}, {apartment_number}')

print(currency + age)


# G
def print_hello():
    print("Hello")


def calculate():
    result = 5 + 3.2
    print(result)


print_hello()
calculate()


# H

def get_name():
    name = input("What is your name? ")
    print(f'{name}')


def calculator():
    cal = int(input(" choose a random number to be divided by 2 "))
    print(cal / 2)


get_name()
calculator()


# l

def addon():
    first_num = int(input(" Choose the first number "))
    second_num = int(input(" Choose the second number "))
    print(first_num + second_num)


def string_spacer():
    first_string = str(input(" Choose a random word "))
    second_string = str(input(" Choose the second word "))
    print(f'{first_string} {second_string}')


addon()
string_spacer()
