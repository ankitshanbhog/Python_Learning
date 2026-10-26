import json

student ={
    "Name" : "Ankit",
    "Marks" : 99,
    "enrolled" : True,    
}

json_text = json.dumps(student)

print(json_text)

print(type(student))
print(type(json_text))


plant ={
    "name" : "Tulsi",
    "medicinal" : True,
    "uses" : ["coush-releif" , "traditional remedies"]  
}

with open("plants_data.txt","w",encoding="utf-8") as file:
    json.dump(plant,file,indent=4)


with open("plants_data.txt","r",encoding="utf-8") as file:
    result = json.load(file)


print(result)
print(result["name"])
print(result["medicinal"])

