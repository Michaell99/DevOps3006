names = ["Tom", "zac", "john", "Michael"]
print(list(range(17, 2, -3)))

for name in names:
    if name == "zac":
        continue
    print(name)

a = 0
while a < 5:
    print(a)
    a = a + 1
    if a == 2:
        break

