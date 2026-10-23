import csv

with open("students.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Marks","City"])
    writer.writerow(["Max",100,"Amsterdam"])
    writer.writerow(["Ankit",95,"Amsterdam"])

with open("students.csv","r",newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
