students = {
    "Arun": [80, 75, 90],
    "Maya": [60, 55, 70],
    "Ravi": [30, 40, 35]
}

def calculate_average(marks):
    
    if(len(marks) == 0):
        return 0.0
    
    sum = 0
    avg = 0
    for mark in marks:
        sum+=mark
        avg = sum / len(marks)
    return avg

def get_status(average,pass_mark=40):

    if(average >= pass_mark):
        return "Pass"
    else:
        return "Fail"

def print_report(name , marks, pass_mark =40):
    
    Student_name = name
    Average_marks = calculate_average(marks)
    status = get_status(Average_marks , pass_mark
                        )
    
    print("Student :" , Student_name)
    print("Average :" , Average_marks)
    print("Status  :" , status )


for student in students:
    print_report(student , students[student] , pass_mark=40)


def add_student(name,marks,students):
    students[name] = marks


add_student("Priya", [85, 90, 95], students)

def show_summary(**kwargs):
    for key , value in kwargs.items():
        print(key," : ",value)

print_report("Priya", [85, 90, 95])

show_summary(
    total_students=len(students),
    subject="Python",
    highest_student="Priya"
)