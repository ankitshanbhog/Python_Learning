file = open("student.txt","r")
content = file.read()
print(content)

file.close()

with open("student.txt","w") as file:
    file.write("Ankit")
    file.write("100")

with open("student.txt","r") as file:
    content = file.read()
    file.close()

print(content)