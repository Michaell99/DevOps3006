is_true = False
a = 2
b = 2.5
str0ne = "one"
strThree = "three"
names = ["Tom", "zac", "john", "Michael"]
other_list = []
if "Ariel" in names:
    print("true")
else:
    print("false")
if len(other_list) > 0:
    print("other list has values")
#another option
name_to_find = "ariel"
if name_to_find in names:
    print(f"we found {name_to_find}")
#////////////////////////////////////////////////////////////////
print(type(a == b))
if a < b and (b != 1 or not str0ne == "moshe" or strThree == "three"):
    print("a is smaller than b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("B is bigger than one")
else:
    print("something")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
print(k == f)
if type(k is int):
    print("I like numbers")
elif type(k is str):
    print("I like strings")
print(k is f)
print(t == e)
print(t is e)
