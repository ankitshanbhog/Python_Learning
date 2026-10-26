import json

try:
    with open("plants.txt","r",encoding="utf-8") as file:
        plant = json.load(file)

except FileNotFoundError:
    print('File not found') 

except json.JSONDecodeError:
    print("File contains invalid json")