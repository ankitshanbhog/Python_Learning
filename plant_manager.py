import json

plants = [{
    "name" : "Tulsi",
    "medicinal" : True,
    "uses" : ["traditional remedies" , "plant study"],
    "image_count" : 20
},
{
    "name" : "Neem",
    "medicinal" : True,
    "uses" : ["antibacterial" , "antifungal"],
    "image_count" : 18
}]

with open("plants.json","w",encoding="utf-8") as file:
    json.dump(plants,file,indent=4)

with open("plants.json","r",encoding="utf-8") as file:
    loaded_plants = json.load(file)



# To add a new Use to a particular plant in the file
# def add_use(loaded_plants,plant_name,new_use):
#     for plant in loaded_plants:
#         if plant["name"].lower() == plant_name.lower():
#             plant["uses"].append(new_use)
#             return True
#     return False

# update_plant = input("Enter the plant to update the uses: ")
# new_use = input("SPecify the new use to be added: ")
# if not new_use:
#      print("Use cannot Empty")

# found = add_use(loaded_plants,update_plant,new_use)

# if found :
#     print("Use added succesfully")
#     with open("plants.json","w",encoding="utf-8") as file:
#             json.dump(loaded_plants,file,indent=4)
# else:
#      print("Not Found")



# To add a new plant to the file 
# def create_dict(new_name,icount):
#     new_dict = {}
#     new_dict["name"] = new_name
#     new_dict["medicinal"] = True
#     new_dict["uses"] = []
#     new_dict["image_count"] = icount
#     return new_dict

# new = input("Enter the name of the new plant: ")
# img_count = int(input("Enter the total image count: "))

# plant_add = create_dict(new,img_count)
# loaded_plants.append(plant_add)

# with open("plants.json","w",encoding="utf-8") as file:
#     json.dump(loaded_plants,file,indent=4)



# To view every plants in the file

def view_plants(loaded_plants):
    for pl in loaded_plants:
        print(
            f"Plant: {pl['name']}\n"
            f"Medicinal: {pl['medicinal']}\n"
            f"Uses: {pl['uses']}\n"
            f"Image count: {pl['image_count']}\n"
        )
        
view_plants(loaded_plants)  



