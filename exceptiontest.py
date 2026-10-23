class InvalidmarksError(Exception):
    pass

def validate_marks(marks):
    if marks<0 or marks>100:
        raise InvalidmarksError("Enter valid marks!")
    elif marks>=40:
        return "Pass"
    else:
        return "Fail"

try:
    marks = int(input("Enter the marks: "))
    result = validate_marks(marks)
       
except ValueError:
    print("Please enter valid marks :)")

except InvalidmarksError as error:
    print("Invalid marks: ",error)

else:
    print("The result is: " , result)

finally:
    print("Validation attmept Finished! ")