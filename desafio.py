CONSTANT_BONUS = 1000

# Get user input
user = input("Type your name: ")

if user.isdigit():
    print("This is not a valid name ")
    exit()
elif len(user) == 0:
    print("You need to type your name")
    exit()
elif user.isspace():
    print("You typed only spaces")
#user = 33 this is error ??

#Get salary and bonus
salary = float(input("Type your salary: "))

CONSTANT_BONUS = float(input("Type your bonus: "))

