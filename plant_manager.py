import json
import csv

# To add a new Use to a particular plant in the file
def add_use(loaded_plants,plant_name,new_use):
    for plant in loaded_plants:
        if plant["name"].lower() == plant_name.lower():
            plant["uses"].append(new_use)
            return True
    return False

# To add a new plant to the file 
def create_dict(new_name,icount):
    new_dict = {}
    new_dict["name"] = new_name
    new_dict["medicinal"] = True
    new_dict["uses"] = []
    new_dict["image_count"] = icount
    return new_dict

# To view every plants in the file

def view_plants(loaded_plants):
    for pl in loaded_plants:
        print(
            f"Plant: {pl['name']}\n"
            f"Medicinal: {pl['medicinal']}\n"
            f"Uses: {pl['uses']}\n"
            f"Image count: {pl['image_count']}\n"
        )
        
def export_to_csv(loaded_plants):
    with open("plants.csv","w",encoding="utf-8",newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ['name','medicinal','uses','image_count']
        )
        writer.writeheader()
        for p in loaded_plants:
            writer.writerow(p)


def load_plants():
    try:
        with open("plants.json","r",encoding="utf-8") as file:
            loadp = json.load(file)
    except FileNotFoundError:
        print("No saved records found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("The saved file contains invalid JSON.")
        return []
    else:
        return loadp


loaded_plants = load_plants()

while True:
    print("\n======= MediPlant Record Manager ======")
    print("1. View plants")
    print("2. Add a plant")
    print("3. Add a use to a plant")
    print("4. Export plants to CSV")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_plants(loaded_plants)

    elif choice == "2":
        new_pl = input("Enter the plant name to add: ")
        img_c = int(input("Enter the image count for the same: "))
        new_dict = create_dict(new_pl,img_c)
        loaded_plants.append(new_dict)
        with open("plants.json","w",encoding="utf-8") as file:
            json.dump(loaded_plants,file,indent=4)
        print("Successfully Added")

    elif choice == "3":
        plant_use = input("Enter the plant for which the use needs to updated: ")
        use = input("Enter the use to be updated: ")
        found = add_use(loaded_plants,plant_use,use)
        if found:
            with open("plants.json","w",encoding="utf-8") as file:
                json.dump(loaded_plants,file,indent=4)
            print("Updated the plant use! ")
        else:
            print("No plant found")

    elif choice == "4":
        export_to_csv(loaded_plants)

    elif choice == "5":
        print("Over and Out !")
        break

    else:
        print("Invalid Choice")

