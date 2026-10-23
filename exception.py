# try:
#     number= int(input("Enter a number: "))
#     print(100/number)
# except ZeroDivisionError:
#     print("You cant divide by zero")

# except ValueError:
#     print("Please enter a valid integer")


try:
    number = int("25")
except ValueError:
    print("Enter a valid number")
else:
    print("Successful conversion",number)