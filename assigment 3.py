try:
    a = 1 / 0
except ZeroDivisionError:
    print("cant be divided by zero")

# 3 Yes try can come with except and finally

# 4 except can handly all types of exceptions

# 5 This type of exception handler is a bad practice it doesn't show us all the information we need.

# 6 in except zerodivisionerror handler the zero division error can be handled and in IoError the input output
# errors can be handled

# 7
my_file = open("C:/Users/user/PycharmProjects/deops3006new/Michael.txt", 'w')
my_file.close()

# 8
my_file = open("C:/Users/user/PycharmProjects/deops3006new/Michael.txt", 'w')
my_file.write("My name is Michael and I want to be a good Devops Engineer")
my_file.close()

# 9
my_file = open("C:/Users/user/PycharmProjects/deops3006new/Michael.txt", 'r')
str = my_file.read()
print(str)
my_file.close()

# 10
my_file2 = open("C:/Users/user/PycharmProjects/deops3006new/MichaelHebrew.txt", 'w', encoding='utf-8')
my_file2.write("שלום")
my_file2.close()

my_file2 = open("C:/Users/user/PycharmProjects/deops3006new/MichaelHebrew.txt", 'r', encoding='utf-8')
info = my_file2.read()
print(info)
