def greet_name(name, excluded_name, greeting_word):
    if name != excluded_name:
        print(f"{greeting_word}{name}")


greet_name("moshe ", ",michael", "bonjour ")


def greet_name(name, excluded_name="michael", greeting_word="hello"):
    if name != excluded_name:
        return f"{greeting_word}{name}"


def multiply(x, y):
    result = x * y
    return result


user_input = input("enter you name:")
print(greet_name(user_input))

print(greet_name(" Rotem"))
bla = multiply(10, 4)
print(bla)

