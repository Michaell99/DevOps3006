import ast
a= "{'name': 'avi'}"
my_file = open("config.json")
c = dict(ast.literal_eval(my_file.read()))

print(c["name"])

with open("names.txt") as my_file:
    for name in my_file.readlines():
        print(name.strip())

