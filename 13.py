my_file = open("names.txt", "a")
current_name = input("enter your name: ")
my_file.write(current_name + "\n")
my_file.close()


def show_names():
    my_file = open("names.txt")
    for name in my_file.readlines():
        print(name, end="")
    my_file.close()

