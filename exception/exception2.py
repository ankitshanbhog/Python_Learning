try:
    marks=150

    if marks<0 or marks>100:
        raise ValueError("Marks must be bewteen 0 and 100")
    print("Marks accepted")

except ValueError as error:
    print("Invalid marks: ",error)

print("Program continues")
